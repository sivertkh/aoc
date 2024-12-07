# AOC 2024
# --- Day 7: Bridge Repair ---

import operator


def sum_exists(target, cur_sum, numbers, operators):

    if not numbers:
        return target == cur_sum

    if cur_sum > target:
        return False

    return any(
        sum_exists(target, op(cur_sum, numbers[0]), numbers[1:], operators)
        for op in operators
    )


def sum_of_valid(data, operators):
    return sum(
        [
            target
            for target, numbers in data
            if sum_exists(target, 0, numbers, operators)
        ]
    )


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        data = [x.split(":") for x in fp.read().split("\n") if x]
        data = [[int(x), list(map(int, y.strip().split()))] for x, y in data]

    return sum_of_valid(data, [operator.add, operator.mul]), sum_of_valid(
        data, [operator.add, operator.mul, lambda a, b: int(f"{a}{b}")]
    )


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 12940396350192
assert part_2 == 106016735664498
