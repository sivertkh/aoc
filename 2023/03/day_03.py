# AOC 2023
# --- Day 3: Gear Ratios ---

from re import finditer

import numpy as np


def is_valid_nr(m, nr, x, y) -> bool:
    if not nr:
        return False

    if len(nr) > 3:
        raise ValueError

    x_start = x - len(nr)
    x_end = x + 1
    if x_start < 0:
        # Do not check before the start
        x_start = 0
    if x_end >= len(m[0]):
        # Do not check after the end
        x_end = x

    y_start = y - 1 if y - 1 >= 0 else y
    y_end = y + 1 if y + 1 <= len(m[0]) else y
    a = m[y_start : y_end + 1, x_start : x_end + 1]

    return any([any([not i.isdigit() and i != "." for i in j]) for j in a])


def solve_part_1(s):
    part_1 = 0
    for y in range(len(s)):
        cur_nr = []
        for x in range(len(s[0])):
            cur_chr = s[y][x]
            if cur_chr.isdigit():
                cur_nr.append(cur_chr)
                continue

            if not s[y][x].isdigit() and not cur_nr:
                # No number at start of line
                continue

            if not s[y][x].isdigit():
                if is_valid_nr(s, cur_nr, x - 1, y):
                    part_1 += int("".join(cur_nr))
                cur_nr = []

        if cur_nr and is_valid_nr(s, cur_nr, x, y):
            part_1 += int("".join(cur_nr))
        cur_nr = []

    return part_1


def solve_part_2(s):
    res = 0
    for x, y in list(zip(*np.where(s == "*"))):
        area = s[x - 1 : x + 2, y - 3 : y + 4]
        nr = []
        for i in range(3):
            for match in finditer(r"\d+", "".join(area[i])):
                start, end = match.span()
                end = end - 1
                if (2 <= start <= 4) or (2 <= end <= 4):
                    nr.append(int(match.group()))

        if len(nr) == 2:
            res += nr[0] * nr[1]
    return res


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        s = np.array([list(x.strip("\n")) for x in fp.readlines() if x])

    return solve_part_1(s), solve_part_2(s)


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 527369
assert part_2 == 73074886
