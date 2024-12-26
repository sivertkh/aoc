# AOC 2024
# --- Day 16: Reindeer Maze ---

import collections as coll

import networkx as nx
import numpy as np


def create_graph(data: np.array) -> nx.Graph:
    """Generate graph of the maze.

    Turns are handled by dividing N/S and E/W into there own "layer".
    A turn then become a edge between the two layers.
    """

    s_x, s_y = next(zip(*np.where(data == "S")))
    e_x, e_y = next(zip(*np.where(data == "E")))

    data[s_x][s_y] = "."
    data[e_x][e_y] = "."

    edges = []
    check_pos = coll.deque([(s_x, s_y, True)])
    visited = set()

    loop_iter = 0

    while check_pos:
        loop_iter += 1
        cur_node = check_pos.popleft()
        x, y, lower_level = cur_node
        visited.add((x, y, lower_level))
        if lower_level:
            # On the "lower" E/W plane
            if data[x][y + 1] == ".":
                to_node = (x, y + 1, lower_level)
                edges.append((cur_node, to_node, 1))

                if to_node not in visited and to_node not in check_pos:
                    check_pos.append(to_node)

            if data[x][y - 1] == ".":
                to_node = (x, y - 1, lower_level)
                edges.append((cur_node, to_node, 1))

                if to_node not in visited and to_node not in check_pos:
                    check_pos.append(to_node)

            if data[x - 1][y] == "." or data[x + 1][y] == ".":
                to_node = (x, y, not lower_level)
                edges.append((cur_node, to_node, 1000))
                if to_node not in visited and to_node not in check_pos:
                    check_pos.append(to_node)

        else:
            # On the "higher" N/S plane
            if data[x - 1][y] == ".":
                to_node = (x - 1, y, lower_level)
                edges.append((cur_node, to_node, 1))

                if to_node not in visited and to_node not in check_pos:
                    check_pos.append(to_node)

            if data[x + 1][y] == ".":
                to_node = (x + 1, y, lower_level)
                edges.append((cur_node, to_node, 1))

                if to_node not in visited and to_node not in check_pos:
                    check_pos.append(to_node)

            if data[x][y - 1] == "." or data[x][y + 1] == ".":
                to_node = (x, y, not lower_level)
                edges.append((cur_node, to_node, 1000))
                if to_node not in visited and to_node not in check_pos:
                    check_pos.append(to_node)

    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    return G


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        data = np.array([list(x) for x in fp.read().split("\n") if x])

    s_x, s_y = next(zip(*np.where(data == "S")))
    e_x, e_y = next(zip(*np.where(data == "E")))

    G = create_graph(data)

    path_1 = nx.shortest_path_length(
        G, (s_x, s_y, True), (e_x, e_y, False), weight="weight"
    )
    path_2 = nx.shortest_path_length(
        G, (s_x, s_y, True), (e_x, e_y, True), weight="weight"
    )

    if path_1 < path_2:
        res_1 = path_1
        paths = nx.all_shortest_paths(
            G, (s_x, s_y, True), (e_x, e_y, False), weight="weight"
        )
    else:
        res_1 = path_2
        paths = nx.all_shortest_paths(
            G, (s_x, s_y, True), (e_x, e_y, True), weight="weight"
        )

    res_2 = set()
    for p in paths:
        for x, y, _ in p:
            res_2.add((x, y))

    return res_1, len(res_2)


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
    assert part_1 == 93436
    assert part_2 == 486
