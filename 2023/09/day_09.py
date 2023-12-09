# AOC 2023
# --- Day 9: Mirage Maintenance ---

import numpy as np


def solve():
    part_1 = 0
    part_2 = 0

    with open("input.txt") as fp:
        s = fp.readlines()

    data = np.array([list(map(int, x.split())) for x in s if x])

    for x in data:
        diff_arrays = [x]
        cur_array = x

        while True:
            cur_diff = np.diff(cur_array)
            diff_arrays.append(cur_diff)
            if not np.any(cur_diff):
                break
            cur_array = cur_diff

        part_1 += np.cumsum([x[-1] for x in diff_arrays][::-1])[-1]

        tmp = [x[0] for x in diff_arrays][::-1]
        diff = [0]
        for i in range(1, len(tmp)):
            diff.append(tmp[i] - diff[-1])
        part_2 += diff[-1]

    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 2101499000
assert part_2 == 1089
