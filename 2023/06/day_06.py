# AOC 2023
# --- Day 6: Wait For It ---

import functools
from typing import List


def find_race_wins(d: List[int], t: List[int]) -> int:
    res = []
    for x in range(len(t)):
        for y in range(t[x]):
            if y * (t[x] - y) > d[x]:
                res.append(t[x] - y * 2 + 1)
                break

    return functools.reduce((lambda x, y: x * y), res)


def solve():
    with open("input.txt") as fp:
        s = fp.readlines()

    t = list(map(int, s[0].split()[1:]))
    d = list(map(int, s[1].split()[1:]))

    part_1 = find_race_wins(d, t)
    part_2 = find_race_wins([int("".join(map(str, d)))], [int("".join(map(str, t)))])

    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 512295
assert part_2 == 36530883
