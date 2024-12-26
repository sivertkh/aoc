# AOC 2024
# --- Day 1: Historian Hysteria ---

import collections as coll
import numpy as np


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        data = np.sort(
            [list(map(int, x.split())) for x in fp.read().split("\n") if x], axis=0
        )
    c = coll.Counter(data[:, 1])
    return np.sum(np.absolute(np.diff(data))), sum([x * c[x] for x in data[:, 0]])


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
    assert part_1 == 2057374
    assert part_2 == 23177084
