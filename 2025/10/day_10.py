"""
AOC 2025
--- Day 10: Factory ---
"""

from z3 import Optimize, Int, Sum, sat


def min_light_presses(target_state: tuple[bool], buttons: tuple[tuple[int]]) -> int:
    button_presses = [Int(f"button_{i}") for i in range(len(buttons))]

    s = Optimize()
    # No negative presses
    s.add(*[presses >= 0 for presses in button_presses])

    for pos, target_value in enumerate(target_state):
        total = Sum(
            [button_presses[i] for i, button in enumerate(buttons) if pos in button]
        )
        s.add(total % 2 == target_value)

    # Minimize total button presses
    total_presses = Sum(button_presses)
    s.minimize(total_presses)

    if s.check() == sat:
        model = s.model()
        return sum(model[v].as_long() for v in model)

    print("No solution!")
    return -1


def min_button_presses(target_state: tuple[bool], buttons: tuple[tuple[int]]) -> int:
    button_presses = [Int(f"button_{i}") for i in range(len(buttons))]

    s = Optimize()
    # No negative presses constraint
    s.add(*[presses >= 0 for presses in button_presses])

    for pos, target_value in enumerate(target_state):
        total = Sum(
            [button_presses[i] for i, button in enumerate(buttons) if pos in button]
        )
        s.add(total == target_value)

    # Minimize total button presses
    total_presses = Sum(button_presses)
    s.minimize(total_presses)

    if s.check() == sat:
        model = s.model()
        return sum(model[v].as_long() for v in model)

    print("No solution!")
    return -1


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        data = [x.split() for x in fp.read().split("\n") if x]

    instructions = []

    for d in data:
        lights = tuple(True if x == "#" else False for x in list(d[0][1:-1]))
        buttons = tuple(tuple(map(int, x[1:-1].split(","))) for x in d[1:-1])
        jolts = tuple(map(int, d[-1][1:-1].split(",")))
        instructions.append((lights, buttons, jolts))

    part_1_res = 0
    part_2_res = 0

    for lights, buttons, jolts in instructions:
        part_1_res += min_light_presses(lights, buttons)
        part_2_res += min_button_presses(jolts, buttons)

    return part_1_res, part_2_res


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

    assert part_1 == 432
    assert part_2 == 18011
