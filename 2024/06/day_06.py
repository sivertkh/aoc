# AOC 2024
#

import networkx as nx
import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
import numpy as np
import functools


def solve_part_1(data):

    guard_x, guard_y = np.where(data == "^")
    visited = []
    cur_x = guard_x[0]
    cur_y = guard_y[0]

    data[cur_x][cur_y] = "."
    direction = "u"
    turn = {
        "u": "r",
        "r": "d",
        "d": "l",
        "l": "u",
    }

    visited.append([cur_x, cur_y, direction])

    while True:
        # check if we can move in the direction we are faceing

        # print(f"In {cur_x},{cur_y} facing {direction}")

        match direction:
            case "u":
                if cur_x - 1 < 0:
                    print("outside of map!!")
                    break
                elif data[cur_x - 1][cur_y] == ".":
                    cur_x = cur_x - 1
                else:
                    direction = turn[direction]
            case "d":
                if cur_x + 1 >= len(data):
                    print("outside of map!!")
                    break
                elif data[cur_x + 1][cur_y] == ".":
                    cur_x = cur_x + 1
                else:
                    direction = turn[direction]
            case "l":
                if cur_y - 1 < 0:
                    print("outside of map!!")
                    break

                elif data[cur_x][cur_y - 1] == ".":
                    cur_y = cur_y - 1
                else:
                    direction = turn[direction]
            case "r":
                if cur_y + 1 >= len(data[0]):
                    print("outside of map!!")
                    break
                elif data[cur_x][cur_y + 1] == ".":
                    cur_y = cur_y + 1
                else:
                    direction = turn[direction]

        if [cur_x, cur_y, direction] in visited:
            print("Return back!!")
            break
        visited.append([cur_x, cur_y, direction])

    test = set(f"{x[0]},{x[1]}" for x in visited)

    return len(test)


def is_cycle(data):

    guard_x, guard_y = np.where(data == "^")

    print(guard_x)
    visited = []
    cur_x = guard_x[0]
    cur_y = guard_y[0]

    data[guard_x[0]][guard_y[0]] = "."
    direction = "u"
    turn = {
        "u": "r",
        "r": "d",
        "d": "l",
        "l": "u",
    }

    visited.append([cur_x, cur_y, direction])

    while True:
        # check if we can move in the direction we are facing
        match direction:
            case "u":
                if cur_x - 1 < 0:
                    data[guard_x[0]][guard_y[0]] = "^"
                    return False
                elif data[cur_x - 1][cur_y] == ".":
                    cur_x = cur_x - 1
                else:
                    direction = turn[direction]
            case "d":
                if cur_x + 1 >= len(data):
                    data[guard_x[0]][guard_y[0]] = "^"
                    return False
                elif data[cur_x + 1][cur_y] == ".":
                    cur_x = cur_x + 1
                else:
                    direction = turn[direction]
            case "l":
                if cur_y - 1 < 0:
                    data[guard_x[0]][guard_y[0]] = "^"
                    return False
                elif data[cur_x][cur_y - 1] == ".":
                    cur_y = cur_y - 1
                else:
                    direction = turn[direction]
            case "r":
                if cur_y + 1 >= len(data[0]):
                    data[guard_x[0]][guard_y[0]] = "^"

                    return False
                elif data[cur_x][cur_y + 1] == ".":
                    cur_y = cur_y + 1
                else:
                    direction = turn[direction]

        if [cur_x, cur_y, direction] in visited:
            print("Found cycle!")
            data[guard_x[0]][guard_y[0]] = "^"
            return True
        visited.append([cur_x, cur_y, direction])


def solve_part_2(data):
    guard_x, guard_y = np.where(data == "^")
    visited = []
    cur_x = guard_x[0]
    cur_y = guard_y[0]

    data[cur_x][cur_y] = "."
    direction = "u"
    turn = {
        "u": "r",
        "r": "d",
        "d": "l",
        "l": "u",
    }

    visited.append([cur_x, cur_y, direction])

    while True:
        match direction:
            case "u":
                if cur_x - 1 < 0:
                    # outside of map!
                    break
                elif data[cur_x - 1][cur_y] == ".":
                    cur_x = cur_x - 1
                else:
                    direction = turn[direction]
            case "d":
                if cur_x + 1 >= len(data):
                    # outside of map!
                    break
                elif data[cur_x + 1][cur_y] == ".":
                    cur_x = cur_x + 1
                else:
                    direction = turn[direction]
            case "l":
                if cur_y - 1 < 0:
                    # outside of map!
                    break
                elif data[cur_x][cur_y - 1] == ".":
                    cur_y = cur_y - 1
                else:
                    direction = turn[direction]
            case "r":
                if cur_y + 1 >= len(data[0]):
                    # outside of map!
                    break
                elif data[cur_x][cur_y + 1] == ".":
                    cur_y = cur_y + 1
                else:
                    direction = turn[direction]

        if [cur_x, cur_y, direction] in visited:
            # Road already traveled
            break
        visited.append([cur_x, cur_y, direction])

    data[guard_x[0]][guard_y[0]] = "^"
    all_visited = set(f"{x[0]},{x[1]}" for x in visited)

    res = 0
    for i, v in enumerate(all_visited):
        print(f"Checking pos {i}/{len(all_visited)}")
        x, y = map(int, v.split(","))

        if x == guard_x[0] and y == guard_y[0]:
            continue

        data[x][y] = "#"
        if is_cycle(data):
            res += 1
        data[x][y] = "."

    return res


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        data = np.array([list(x) for x in fp.read().split("\n") if x])

    print(data)

    return (
        solve_part_1(data.copy()),
        0,
    )  # solve_part_2(data)


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")

assert part_1 == 4663
assert part_2 == 1530
