# --- Day 22: Mode Maze ---
# Part 1 - ok
# Part 2 - ok

import numpy as np
import networkx as nx
from collections import deque
import heapq


def create_graph(cave, target_x, target_y):
    # 0 = rocky, 1 = wet, 2 = narrow
    # 0 = climing, 1 = neither, 2 = torch

    allowd_tools = {
        0: {0, 2},
        1: {0, 1},
        2: {1, 2},
    }

    graph = nx.Graph()
    for y in range(len(cave)-1):
        for x in range(len(cave[0])-1):
            for new_y, new_x in [(y+1, x), (y, x+1)]:
                cur_allowed_tools = allowd_tools[cave[y][x]]
                to_allowed_tools = allowd_tools[cave[new_y][new_x]]

                for cur_tool in cur_allowed_tools:
                    for to_tool in to_allowed_tools:
                        if cur_tool == to_tool:
                            graph.add_edge((y, x, cur_tool),
                                           (new_y, new_x, to_tool), weight=1)
                        elif cur_tool in to_allowed_tools:
                            graph.add_edge((y, x, cur_tool),
                                           (new_y, new_x, to_tool), weight=8)

    return nx.dijkstra_path_length(graph, (0, 0, 2), (target_y, target_x, 2))


def main():
    with open('input.txt') as fp:
        depth = int(fp.readline().split(' ')[1])

        target_x, target_y = [int(x) for x in fp.readline().split(
            ' ')[1].rstrip('\n').split(',')]

    # The "buffer" size might not be correct for all inputs
    buffer = 20
    gi = np.array([[0 for x in range(target_x+buffer)]
                   for y in range(target_y+buffer)])
    cave = np.array([[0 for x in range(target_x+buffer)]
                     for y in range(target_y+buffer)])
    ei = np.array([[0 for x in range(target_x+buffer)]
                   for y in range(target_y+buffer)])

    for y in range(target_y+buffer):
        for x in range(target_x+buffer):
            if x == 0 and y == 0:
                gi[y][x] = 0
            elif x == target_x and y == target_y:
                gi[y][x] = 0
            elif x == 0:
                gi[y][x] = 48271 * y
            elif y == 0:
                gi[y][x] = 16807 * x
            else:
                gi[y][x] = ei[y][x-1] * ei[y-1][x]

            ei[y][x] = ((gi[y][x] + depth) % 20183)
            cave[y][x] = ei[y][x] % 3

    risk = 0
    for y in range(target_y+1):
        for x in range(target_x+1):
            risk += cave[y][x]

    print(f'Part 1: {risk}')
    print(f'Part 2: {create_graph(cave, target_x, target_y)}')


if __name__ == "__main__":
    main()
