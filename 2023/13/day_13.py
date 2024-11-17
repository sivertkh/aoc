"""
AOC 2023
--- Day 13: Point of Incidence ---
"""

import numpy as np


def solve():
    res_1 = 0
    res_2 = 0

    with open("input.txt", encoding="utf-8") as fp:
        s = fp.read()

    patterns = [
        np.array([list(y) for y in x.split("\n") if y]) for x in s.split("\n\n") if x
    ]

    for pattern in patterns:
        # Rows
        for x in range(1, len(pattern)):
            slice_size = min(x, len(pattern) - x)
            equal = pattern[x - slice_size : x] == np.flip(
                pattern[x : x + slice_size], 0
            )
            match np.size(equal) - np.count_nonzero(equal):
                case 0:
                    res_1 += 100 * x
                case 1:
                    res_2 += 100 * x

        # Columns
        for x in range(1, len(pattern[0])):
            slice_size = min(x, len(pattern[0]) - x)
            equal = pattern[:, x - slice_size : x] == np.flip(
                pattern[:, x : x + slice_size], 1
            )
            match np.size(equal) - np.count_nonzero(equal):
                case 0:
                    res_1 += x
                case 1:
                    res_2 += x

    return res_1, res_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 34100
assert part_2 == 33106
