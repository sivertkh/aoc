# AOC 2023
# --- Day 1: Historian Hysteria ---

import collections as coll
import numpy as np


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        data = np.sort(
            [list(map(int, x.split("   "))) for x in fp.read().split("\n") if x], axis=0
        )
    c = coll.Counter(data[:, 1])
    return sum([abs(a - b) for a, b in data]), sum([x * c[x] for x in data[:, 0]])


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 2057374
assert part_2 == 23177084
