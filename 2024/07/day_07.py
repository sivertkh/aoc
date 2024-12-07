# AOC 2024
# --- Day 7: Bridge Repair ---


def sum_part_1(target, cur_sum, numbers):
    if not numbers:
        return target == cur_sum

    if cur_sum > target:
        return False

    return sum_part_1(target, cur_sum * numbers[0], numbers[1:]) or sum_part_1(
        target, cur_sum + numbers[0], numbers[1:]
    )


def sum_part_2(target, cur_sum, numbers):
    if not numbers:
        return target == cur_sum

    if cur_sum > target:
        return False

    return (
        sum_part_2(target, int(f"{cur_sum}{numbers[0]}"), numbers[1:])
        or sum_part_2(target, cur_sum * numbers[0], numbers[1:])
        or sum_part_2(target, cur_sum + numbers[0], numbers[1:])
    )


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        data = [x.split(":") for x in fp.read().split("\n") if x]
        data = [[int(x), list(map(int, y.strip().split()))] for x, y in data]

    p1_targets = [
        target
        for target, numbers in data
        if sum_part_1(target, numbers[0], numbers[1:])
    ]
    p1 = sum(p1_targets)

    p2 = p1 + sum(
        [
            target
            for target, numbers in data
            if target not in p1_targets and sum_part_2(target, numbers[0], numbers[1:])
        ]
    )
    return p1, p2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 12940396350192
assert part_2 == 106016735664498
