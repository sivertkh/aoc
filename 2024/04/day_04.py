# AOC 2023
# --- Day 4: Ceres Search ---

import numpy as np


def solve_part_1(data):

    res = 0
    for x in data:
        s = "".join(x)
        res += s.count("XMAS") + s[::-1].count("XMAS")

    for x in data.T:
        s = "".join(x)
        res += s.count("XMAS") + s[::-1].count("XMAS")

    flipped = np.fliplr(data)
    offset = len(data[0])
    for x in range(-offset, offset + 1):
        s = "".join(np.diagonal(data, offset=x))
        res += s.count("XMAS") + s[::-1].count("XMAS")
        s = "".join(np.diagonal(flipped, offset=x))
        res += s.count("XMAS") + s[::-1].count("XMAS")

    return res


def solve_part_2(data):

    targets = [["M", "A", "S"], ["S", "A", "M"]]
    res = 0

    for a in np.lib.stride_tricks.sliding_window_view(data, (3, 3)):
        for b in a:
            if (
                b.diagonal().tolist() in targets
                and np.fliplr(b).diagonal().tolist() in targets
            ):
                res += 1
    return res


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        data = np.array([list(x) for x in fp.read().split("\n") if x])

    return solve_part_1(data), solve_part_2(data)


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 2524
assert part_2 == 1873
