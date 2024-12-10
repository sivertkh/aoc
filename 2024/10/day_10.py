# AOC 2024
# --- Day 10: Hoof It ---

import networkx as nx
import numpy as np


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        data = np.array([list(map(int, list(x))) for x in fp.read().split("\n") if x])

    G = nx.DiGraph()

    # pylint: disable=C0200
    for x in range(len(data)):
        for y in range(len(data[0])):
            cur = data[x][y]
            if x - 1 >= 0 and data[x - 1][y] - cur == 1:
                G.add_edge((x, y), (x - 1, y))
            if x + 1 < len(data) and data[x + 1][y] - cur == 1:
                G.add_edge((x, y), (x + 1, y))
            if y - 1 >= 0 and data[x][y - 1] - cur == 1:
                G.add_edge((x, y), (x, y - 1))
            if y + 1 < len(data[0]) and data[x][y + 1] - cur == 1:
                G.add_edge((x, y), (x, y + 1))

    p1, p2 = 0, 0
    for end in zip(*np.where(data == 9)):
        for start in zip(*np.where(data == 0)):
            s = (start[0], start[1])
            e = (end[0], end[1])
            try:
                p = len(list(nx.all_simple_paths(G, s, e)))
                if p > 0:
                    p1 += 1
                    p2 += p
            except nx.exception.NetworkXNoPath:
                continue
    return p1, p2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 548
assert part_2 == 1252
