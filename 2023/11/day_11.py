# AOC 2023
# --- Day 11: Cosmic Expansion ---

import itertools as it
import numpy as np


def solve():
    part_1 = 0
    part_2 = 0

    with open("input.txt") as fp:
        data = np.array([list(x.strip()) for x in fp.readlines() if x])

    rows_exp = {i for i, x in enumerate(data) if np.all(x == ".")}
    col_exp = {i for i, x in enumerate(data.T) if np.all(x == ".")}

    for n1, n2 in it.combinations(np.argwhere(data == "#"), 2):
        x_jmp = len(
            rows_exp.intersection(
                set(
                    range(n1[0], n2[0] + 1)
                    if n1[0] < n2[0]
                    else range(n2[0], n1[0] + 1)
                )
            )
        )

        y_jmp = len(
            col_exp.intersection(
                set(
                    range(n1[1], n2[1] + 1)
                    if n1[1] < n2[1]
                    else range(n2[1], n1[1] + 1)
                )
            )
        )

        dist = abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])
        part_1 += dist + x_jmp + y_jmp
        part_2 += dist + x_jmp * (1000000 - 1) + y_jmp * (1000000 - 1)

    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 9623138
assert part_2 == 726820169514
