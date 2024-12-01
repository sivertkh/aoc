# AOC 2023
# --- Day 23: A Long Walk ---

import collections as coll

import networkx as nx
import numpy as np


def solve_part_1(data):

    G = nx.DiGraph()

    coords = np.where(data != "#")
    cords_lookup = {}
    for i in range(len(coords[0])):
        x = coords[0][i]
        y = coords[1][i]
        cords_lookup[f"{x},{y}"] = data[x][y]

    for k, v in cords_lookup.items():
        x, y = map(int, k.split(","))

        match v:
            case ".":
                if f"{x-1},{y}" in cords_lookup and cords_lookup[f"{x-1},{y}"] in [
                    ".",
                    "^",
                ]:
                    G.add_edge(f"{x},{y}", f"{x-1},{y}")
                if f"{x+1},{y}" in cords_lookup and cords_lookup[f"{x+1},{y}"] in [
                    ".",
                    "v",
                ]:
                    G.add_edge(f"{x},{y}", f"{x+1},{y}")
                if f"{x},{y-1}" in cords_lookup and cords_lookup[f"{x},{y-1}"] in [
                    ".",
                    "<",
                ]:
                    G.add_edge(f"{x},{y}", f"{x},{y-1}")
                if f"{x},{y+1}" in cords_lookup and cords_lookup[f"{x},{y+1}"] in [
                    ".",
                    ">",
                ]:
                    G.add_edge(f"{x},{y}", f"{x},{y+1}")
            case "^":
                G.add_edge(f"{x},{y}", f"{x-1},{y}")
            case "v":
                G.add_edge(f"{x},{y}", f"{x+1},{y}")
            case "<":
                G.add_edge(f"{x},{y}", f"{x},{y-1}")
            case ">":
                G.add_edge(f"{x},{y}", f"{x},{y+1}")

    return (
        max(map(len, nx.all_simple_paths(G, "0,1", f"{len(data)-1},{len(data[0])-2}")))
        - 1
    )


def solve_part_2(data):
    G = nx.Graph()

    # create nodes
    coords = np.where(data != "#")
    valid_positions = set()

    for i in range(len(coords[0])):
        valid_positions.add((coords[0][i], coords[1][i]))

    paths = coll.deque()
    paths.append([0, 1, 0, 1])
    visited = set()

    while paths:
        x, y, start_x, start_y = paths.popleft()
        steps = 0

        while True:
            possible_moves = [
                w
                for w in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                if w in valid_positions
            ]
            steps += 1

            if len(possible_moves) == 1:
                next_x, next_y = possible_moves[0]
                if x == 0:
                    visited.add((x, y))
                    x, y = possible_moves[0]
                else:
                    visited.add((x, y))
                    visited.add((next_x, next_y))
                    G.add_edge((start_x, start_y), (x, y), weight=steps)
                    break

            elif len(possible_moves) == 2:
                valid_moves = [
                    m
                    for m in possible_moves
                    if m not in visited and m != (start_x, start_y)
                ]

                if len(valid_moves) == 0:
                    # Already visited paths
                    break

                visited.add((x, y))
                x, y = valid_moves[0]
            else:
                G.add_edge((start_x, start_y), (x, y), weight=steps)
                for px, py in [m for m in possible_moves if m not in visited]:
                    paths.append([px, py, x, y])
                break

    return max(
        [
            nx.path_weight(G, path, "weight") - 1
            for path in nx.all_simple_paths(
                G, (0, 1), (len(data) - 1, len(data[0]) - 2)
            )
        ]
    )


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        data = np.array([list(x) for x in fp.read().split("\n") if x])
    return solve_part_1(data), solve_part_2(data)


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 1998
assert part_2 == 6434
