"""
AOC 2025
--- Day 7: Laboratories ---
"""

import math
import itertools

import networkx as nx


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        data = tuple(
            tuple(map(int, x.strip().split(","))) for x in fp.read().split("\n") if x
        )

    distances = []

    for a, b in itertools.combinations(data, 2):
        dist = math.sqrt(
            abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2 + abs(a[2] - b[2]) ** 2
        )
        distances.append([dist, a, b])

    distances.sort(key=lambda x: x[0])
    G = nx.Graph()

    part_1_res = 0
    part_2_res = 0

    for dist, a, b in distances:
        G.add_edge(a, b)
        if len(G.edges) == 1000:
            lengths = [
                len(c)
                for c in sorted(nx.connected_components(G), key=len, reverse=True)
            ]
            part_1_res = lengths[0] * lengths[1] * lengths[2]

        if len(G.nodes) == 1000:
            part_2_res = a[0] * b[0]
            break

    return part_1_res, part_2_res


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

    assert part_1 == 62186
    assert part_2 == 8420405530
