# AOC 2023
# --- Day 19: Aplenty ---

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
import json


def solve():
    part_1 = 0
    part_2 = 0

    with open("input.txt", "r", encoding="utf-8") as fp:
        data = np.array([list(x.strip()) for x in fp.readlines() if x])

    start = np.where(data == "S")
    start_x = int(start[0][0])
    start_y = int(start[1][0])

    current_positions = set()
    current_positions.add((start_x, start_y))

    nr_steps = 64
    for step in range(nr_steps):
        new_positions = set()
        for x, y in current_positions:
            # Up
            if x - 1 >= 0 and data[x - 1][y] != "#":
                new_positions.add((x - 1, y))

            # Down
            if x + 1 < len(data) and data[x + 1][y] != "#":
                new_positions.add((x + 1, y))

            # Left
            if y - 1 >= 0 and data[x][y - 1] != "#":
                new_positions.add((x, y - 1))

            # Down
            if y + 1 < len(data[0]) and data[x][y + 1] != "#":
                new_positions.add((x, y + 1))

        current_positions = new_positions

    return len(current_positions), part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
# assert part_1 == 3615
# assert part_2 ==
