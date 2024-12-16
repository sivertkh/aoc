# AOC 2024
#

import sys


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

sys.setrecursionlimit(10000)


def find_sp(data, x, y, cur_cost, visited, direction):

    if data[x][y] == "E":
        return cur_cost

    costs = []
    visited.append((x, y))

    match direction:
        case "N":
            if (
                x - 1 >= 0
                and (x - 1, y) not in visited
                and data[x - 1][y] in [".", "E"]
            ):
                res = find_sp(data, x - 1, y, cur_cost + 1, visited.copy(), "N")

                if res != -1:
                    costs.append(res)
            # move 90 degrees in both directions
            # Dir = W
            if (
                y - 1 >= 0
                and (x, y - 1) not in visited
                and data[x][y - 1] in [".", "E"]
            ):
                res = find_sp(data, x, y - 1, cur_cost + 1001, visited.copy(), "W")

                if res != -1:
                    costs.append(res)
            # Dir = E
            if (
                y + 1 < len(data[0])
                and (x, y + 1) not in visited
                and data[x][y + 1] in [".", "E"]
            ):
                res = find_sp(data, x, y + 1, cur_cost + 1001, visited.copy(), "E")

                if res != -1:
                    costs.append(res)

        case "S":
            if (
                x + 1 < len(data)
                and (x + 1, y) not in visited
                and data[x + 1][y] in [".", "E"]
            ):
                res = find_sp(data, x + 1, y, cur_cost + 1, visited.copy(), "S")

                if res != -1:
                    costs.append(res)
            # move 90 degrees in both directions
            # Dir = W
            if (
                y - 1 >= 0
                and (x, y - 1) not in visited
                and data[x][y - 1] in [".", "E"]
            ):
                res = find_sp(data, x, y - 1, cur_cost + 1001, visited.copy(), "W")

                if res != -1:
                    costs.append(res)
            # Dir = E
            if (
                y + 1 < len(data[0])
                and (x, y + 1) not in visited
                and data[x][y + 1] in [".", "E"]
            ):
                res = find_sp(data, x, y + 1, cur_cost + 1001, visited.copy(), "E")

                if res != -1:
                    costs.append(res)
        case "E":
            if (
                y + 1 < len(data[0])
                and (x, y + 1) not in visited
                and data[x][y + 1] in [".", "E"]
            ):
                res = find_sp(data, x, y + 1, cur_cost + 1, visited.copy(), "E")

                if res != -1:
                    costs.append(res)

            # move 90 degrees in both directions
            # Dir = N
            if (
                x - 1 >= 0
                and (x - 1, y) not in visited
                and data[x - 1][y] in [".", "E"]
            ):
                res = find_sp(data, x - 1, y, cur_cost + 1001, visited.copy(), "N")

                if res != -1:
                    costs.append(res)
            # Dir = S
            if (
                x + 1 < len(data)
                and (x + 1, y) not in visited
                and data[x + 1][y] in [".", "E"]
            ):
                res = find_sp(data, x + 1, y, cur_cost + 1001, visited.copy(), "S")

                if res != -1:
                    costs.append(res)
        case "W":
            if (
                y - 1 >= 0
                and (x, y - 1) not in visited
                and data[x][y - 1] in [".", "E"]
            ):
                res = find_sp(data, x, y - 1, cur_cost + 1, visited.copy(), "W")

                if res != -1:
                    costs.append(res)
            # move 90 degrees in both directions
            # Dir = N
            if (
                x - 1 >= 0
                and (x - 1, y) not in visited
                and data[x - 1][y] in [".", "E"]
            ):
                res = find_sp(data, x - 1, y, cur_cost + 1001, visited.copy(), "N")

                if res != -1:
                    costs.append(res)

            # Dir = S
            if (
                x + 1 < len(data)
                and (x + 1, y) not in visited
                and data[x + 1][y] in [".", "E"]
            ):
                res = find_sp(data, x + 1, y, cur_cost + 1001, visited.copy(), "S")

                if res != -1:
                    costs.append(res)

    if not costs:
        # No paths to end..
        return -1

    return min(costs)


def graph_version(data):

    s_x, s_y = next(zip(*np.where(data == "S")))
    e_x, e_y = next(zip(*np.where(data == "E")))

    # paths = np.where(data == ".")

    G = nx.DiGraph()

    paths = coll.deque()

    paths.append((s_x, s_y, "E"))

    visited = []

    while paths:
        x, y, direction = paths.popleft()

        visited.append((x, y, direction))

        match direction:
            case "N":
                if (
                    x - 1 >= 0
                    and (x - 1, y, "N") not in visited
                    and data[x - 1][y] in [".", "E"]
                ):
                    j = 1
                    while True:
                        if j >= 0 and data[x - j][y] != "#":
                            j += 1

                    G.add_edge((x, y, "N"), (x - 1, y, "N"), weight=1)
                    paths.append((x - 1, y, "N"))

                # move 90 degrees in both directions
                # Dir = W
                if (
                    y - 1 >= 0
                    and (x, y - 1, "W") not in visited
                    and data[x][y - 1] in [".", "E"]
                ):
                    G.add_edge((x, y, "N"), (x, y - 1, "W"), weight=1001)
                    paths.append((x, y - 1, "W"))

                # Dir = E
                if (
                    y + 1 < len(data[0])
                    and (x, y + 1, "E") not in visited
                    and data[x][y + 1] in [".", "E"]
                ):
                    G.add_edge((x, y, "N"), (x, y + 1, "E"), weight=1001)
                    paths.append((x, y + 1, "E"))

            case "S":
                if (
                    x + 1 < len(data)
                    and (x + 1, y, "S") not in visited
                    and data[x + 1][y] in [".", "E"]
                ):
                    G.add_edge((x, y, "S"), (x + 1, y, "S"), weight=1)
                    paths.append((x + 1, y, "S"))

                # move 90 degrees in both directions
                # Dir = W
                if (
                    y - 1 >= 0
                    and (x, y - 1, "W") not in visited
                    and data[x][y - 1] in [".", "E"]
                ):
                    G.add_edge((x, y, "S"), (x, y - 1, "W"), weight=1001)
                    paths.append((x, y - 1, "W"))

                # Dir = E
                if (
                    y + 1 < len(data[0])
                    and (x, y + 1, "E") not in visited
                    and data[x][y + 1] in [".", "E"]
                ):
                    G.add_edge((x, y, "S"), (x, y + 1, "E"), weight=1001)
                    paths.append((x, y + 1, "E"))

            case "E":
                if (
                    y + 1 < len(data[0])
                    and (x, y + 1, "E") not in visited
                    and data[x][y + 1] in [".", "E"]
                ):
                    G.add_edge((x, y, "E"), (x, y + 1, "E"), weight=1)
                    paths.append((x, y + 1, "E"))

                # move 90 degrees in both directions
                # Dir = N
                if (
                    x - 1 >= 0
                    and (x - 1, y, "N") not in visited
                    and data[x - 1][y] in [".", "E"]
                ):
                    G.add_edge((x, y, "E"), (x - 1, y, "N"), weight=1001)
                    paths.append((x - 1, y, "N"))

                # Dir = S
                if (
                    x + 1 < len(data)
                    and (x + 1, y, "S") not in visited
                    and data[x + 1][y] in [".", "E"]
                ):
                    G.add_edge((x, y, "E"), (x + 1, y, "S"), weight=1001)
                    paths.append((x + 1, y, "S"))

            case "W":
                if (
                    y - 1 >= 0
                    and (x, y - 1, "W") not in visited
                    and data[x][y - 1] in [".", "E"]
                ):
                    G.add_edge((x, y, "W"), (x, y - 1, "W"), weight=1)
                    paths.append((x, y - 1, "W"))

                # move 90 degrees in both directions
                # Dir = N
                if (
                    x - 1 >= 0
                    and (x - 1, y, "N") not in visited
                    and data[x - 1][y] in [".", "E"]
                ):
                    G.add_edge((x, y, "W"), (x - 1, y, "N"), weight=1001)
                    paths.append((x - 1, y, "N"))

                # Dir = S
                if (
                    x + 1 < len(data)
                    and (x + 1, y, "S") not in visited
                    and data[x + 1][y] in [".", "E"]
                ):
                    G.add_edge((x, y, "W"), (x + 1, y, "S"), weight=1001)
                    paths.append((x + 1, y, "S"))

    return G


def solve_part_1(data):
    res = 0

    s_x, s_y = next(zip(*np.where(data == "S")))
    e_x, e_y = next(zip(*np.where(data == "E")))
    print("Graph!!")
    G = graph_version(data)
    print("after creation")
    test1 = nx.shortest_path_length(
        G, (s_x, s_y, "E"), (e_x, e_y, "E"), weight="weight"
    )
    test2 = nx.shortest_path_length(
        G, (s_x, s_y, "E"), (e_x, e_y, "N"), weight="weight"
    )

    return min([test1, test2])


def solve_part_2(data):
    res = 0

    return res


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        data = np.array([list(x) for x in fp.read().split("\n") if x])

    return solve_part_1(data), solve_part_2(data)


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
# assert part_1 ==
# assert part_2 ==
