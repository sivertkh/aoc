# --- Day 6: Signals and Noise ---

import collections as coll
import numpy as np


def load_input():
    with open("input.txt") as fp:
        x = np.array([np.array(list(x.strip())) for x in fp.readlines() if len(x) != 0])
    return x


def solve(d):
    res_part_1 = []
    res_part_2 = []
    for x in range(len(d[0])):
        counter = coll.Counter(d[:, x]).most_common()
        res_part_1.append(counter[0][0])
        res_part_2.append(counter[-1][0])
    return "".join(res_part_1), "".join(res_part_2)


part_1, part_2 = solve(load_input())
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
