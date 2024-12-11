# AOC 2024
# --- Day 11: Plutonian Pebbles ---

import functools


@functools.cache
def stone_count(stone_value, step):

    if step == 0:
        return 1

    if stone_value == 0:
        return stone_count(1, step - 1)

    if len(str(stone_value)) % 2 == 0:
        middle = len(str(stone_value)) // 2
        return stone_count(int(str(stone_value)[:middle]), step - 1) + stone_count(
            int(str(stone_value)[middle:]), step - 1
        )

    return stone_count(stone_value * 2024, step - 1)


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        data = [int(x) for x in fp.readline().split()]

    return sum([stone_count(x, 25) for x in data]), sum(
        [stone_count(x, 75) for x in data]
    )


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 182081
assert part_2 == 216318908621637
