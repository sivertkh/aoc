# AOC 2024
# --- Day 19: Linen Layout ---

import functools


@functools.cache
def possible_combination_count(avail, target: str):
    if not target:
        return 1

    count = 0
    for x in avail:
        if target.startswith(x):
            count += possible_combination_count(
                avail,
                target[len(x) :],
            )

    return count


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        avail, patterns = [x for x in fp.read().split("\n\n") if x]

    avail = tuple(x.strip() for x in avail.split(","))
    patterns = [x.strip() for x in patterns.split("\n") if x]

    p1, p2 = 0, 0
    for x in patterns:
        combinations = possible_combination_count(avail, x)
        if combinations > 0:
            p1 += 1
            p2 += combinations

    return p1, p2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 311
assert part_2 == 616234236468263
