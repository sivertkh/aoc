# AOC 2024
# --- Day 13: Claw Contraption ---

import re
import z3


def min_pres(a: list, b: list, target: list) -> int:
    s = z3.Solver()

    p_a = z3.Int("p_a")
    p_b = z3.Int("p_b")

    s.add(p_a >= 0)
    s.add(p_b >= 0)
    s.add(p_a * a[0] + p_b * b[0] == target[0])
    s.add(p_a * a[1] + p_b * b[1] == target[1])

    if s.check() == z3.sat:
        m = s.model()
        return m[p_a].as_long() * 3 + m[p_b].as_long()
    return 0


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        data = [x for x in fp.read().split("\n\n") if x]

    data = [
        [list(map(int, re.findall(r"\d+", y))) for y in x.split("\n") if y]
        for x in data
        if x
    ]

    p1, p2 = 0, 0
    for d in data:

        a, b, target = d
        p1 += min_pres(a, b, target)

        target = [t + 10000000000000 for t in target]
        p2 += min_pres(a, b, target)

    return p1, p2


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
    assert part_1 == 37901
    assert part_2 == 77407675412647
