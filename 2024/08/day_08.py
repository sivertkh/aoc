# AOC 2024
# --- Day 8: Resonant Collinearity ---

import itertools as it
import numpy as np


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        data = np.array([list(x) for x in fp.read().split("\n") if x])

    antenna_types = set()

    for x in data:
        for y in x:
            if y != ".":
                antenna_types.add(y)

    p1 = set()
    p2 = set()
    for pos in [zip(*np.where(data == x)) for x in antenna_types]:
        for a, b in it.combinations(pos, 2):
            diff_x = abs(a[0] - b[0])
            diff_y = abs(a[1] - b[1])

            p2.add((a[0], a[1]))
            p2.add((b[0], b[1]))

            if a[0] == b[0]:
                if a[1] == b[1]:
                    raise ValueError("Two antennas on the same point")
                elif a[1] < b[1]:
                    if a[1] - diff_y >= 0:
                        p1.add((a[0], a[1] - diff_y))
                    if b[1] + diff_y < len(data[0]):
                        p1.add((b[0], b[1] + diff_y))

                    y = diff_y
                    while b[1] + y < len(data[0]):
                        p2.add((b[0], b[1] + y))
                        y += diff_y
                    y = diff_y
                    while a[1] - y >= 0:
                        p2.add((a[0], a[1] - y))
                        y += diff_y
                else:
                    if a[1] + diff_y < len(data[0]):
                        p1.add((a[0], a[1] + diff_y))
                    if b[1] - diff_y >= 0:
                        p1.add((b[0], b[1] - diff_y))

                    y = diff_y
                    while a[1] + y < len(data[0]):
                        p2.add((a[0], a[1] + y))
                        y += diff_y
                    y = diff_y
                    while b[1] - y >= 0:
                        p1.add((b[0], b[1] - y))
                        y += diff_y
            elif a[0] < b[0]:
                if a[1] == b[1]:
                    if a[0] - diff_x >= 0:
                        p1.add((a[0] - diff_x, a[1]))
                    if b[0] + diff_x < len(data):
                        p1.add((b[0] + diff_x, b[1]))

                    x = diff_x
                    while a[0] - x >= 0:
                        data[a[0] - x][a[1]] = "#"
                        p2.add((a[0] - x, a[1]))
                        x += diff_x
                    x = diff_x
                    with b[0] + x < len(data):
                        p2.add((b[0] + x, b[1]))
                        x += diff_x
                elif a[1] < b[1]:
                    if a[0] - diff_x >= 0 and a[1] - diff_y >= 0:
                        p1.add((a[0] - diff_x, a[1] - diff_y))
                    if b[0] + diff_x < len(data) and b[1] + diff_y < len(data[0]):
                        p1.add((b[0] + diff_x, b[1] + diff_y))

                    x, y = diff_x, diff_y
                    while a[0] - x >= 0 and a[1] - y >= 0:
                        p2.add((a[0] - x, a[1] - y))
                        x += diff_x
                        y += diff_y
                    x, y = diff_x, diff_y
                    while b[0] + x < len(data) and b[1] + y < len(data[0]):
                        p2.add((b[0] + x, b[1] + y))
                        x += diff_x
                        y += diff_y
                else:
                    if a[0] - diff_x >= 0 and a[1] + diff_y < len(data[0]):
                        p1.add((a[0] - diff_x, a[1] + diff_y))
                    if b[0] + diff_x < len(data) and b[1] - diff_y >= 0:
                        p1.add((b[0] + diff_x, b[1] - diff_y))

                    x, y = diff_x, diff_y
                    while a[0] - x >= 0 and a[1] + y < len(data[0]):
                        p2.add((a[0] - x, a[1] + y))
                        x += diff_x
                        y += diff_y
                    x, y = diff_x, diff_y
                    while b[0] + x < len(data) and b[1] - y >= 0:
                        p2.add((b[0] + x, b[1] - y))
                        x += diff_x
                        y += diff_y
            else:
                if a[1] == b[1]:
                    if a[0] + diff_x < len(data):
                        p1.add((a[0] + diff_x, a[1]))
                    if b[0] - diff_x >= 0:
                        p1.add((b[0] - diff_x, b[1]))

                    x = diff_x
                    while a[0] + x < len(data):
                        p2.add((a[0] + x, a[1]))
                        x += diff_x
                    x = diff_x
                    while b[0] - x >= 0:
                        p2.add((b[0] - x, b[1]))
                        x += diff_x

                elif a[1] < b[1]:
                    if a[0] + diff_x < len(data) and a[1] + diff_y < len(data[0]):
                        p1.add((a[0] + diff_x, a[1] + diff_y))
                    if b[0] - diff_x >= 0 and b[1] - diff_y >= 0:
                        p1.add((b[0] - diff_x, b[1] - diff_y))

                    x, y = diff_x, diff_y
                    while a[0] + x < len(data) and a[1] + y < len(data[0]):
                        p2.add((a[0] + x, a[1] + y))
                        x += diff_x
                        y += diff_y
                    x, y = diff_x, diff_y
                    while b[0] - x >= 0 and b[1] - y >= 0:
                        p2.add((b[0] - x, b[1] - y))
                        x += diff_x
                        y += diff_y

                else:
                    if a[0] + diff_x < len(data) and a[1] - diff_y >= 0:
                        p1.add((a[0] + diff_x, a[1] - diff_y))
                    if b[0] - diff_x >= 0 and b[1] + diff_y < len(data[0]):
                        p1.add((b[0] - diff_x, b[1] + diff_y))

                    x, y = diff_x, diff_y
                    while a[0] + x < len(data) and a[1] - y >= 0:
                        p2.add((a[0] + x, a[1] - y))
                        x += diff_x
                        y += diff_y
                    x, y = diff_x, diff_y
                    while b[0] - x >= 0 and b[1] + y < len(data[0]):
                        p2.add((b[0] - x, b[1] + y))
                        x += diff_x
                        y += diff_y

    return len(p1), len(p2)


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 348
assert part_2 == 1221
