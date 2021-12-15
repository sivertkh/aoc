# --- Day 15: Chiton ---

import numpy as np
import networkx as nx


def shortest_path(area):
    FG = nx.DiGraph()
    for i in range(len(area)):
        for j in range(len(area[0])):
            cur_node = f"{i}-{j}"
            if i > 0:
                FG.add_weighted_edges_from([(cur_node, f"{i-1}-{j}", area[i - 1][j])])
            if i < len(area) - 1:
                FG.add_weighted_edges_from([(cur_node, f"{i+1}-{j}", area[i + 1][j])])
            if j > 0:
                FG.add_weighted_edges_from([(cur_node, f"{i}-{j-1}", area[i][j - 1])])
            if j < len(area[0]) - 1:
                FG.add_weighted_edges_from([(cur_node, f"{i}-{j+1}", area[i][j + 1])])
    return nx.dijkstra_path_length(FG, "0-0", f"{len(area)-1}-{len(area[0])-1}")


with open("input.txt") as fp:
    area = [[int(y) for y in x] for x in fp.read().strip().split("\n")]

wrap_func = np.vectorize(lambda x: 1 if x > 9 else x)
area_part_2 = np.array(area)
new_area = area_part_2.copy()
for i in range(4):
    new_area = wrap_func(new_area.copy() + 1)
    area_part_2 = np.concatenate([area_part_2, new_area], axis=1)

new_area = area_part_2.copy()
for i in range(4):
    new_area = wrap_func(new_area.copy() + 1)
    area_part_2 = np.concatenate([area_part_2, new_area], axis=0)

print(f"Part 1: {shortest_path(area)}")
print(f"Part 2: {shortest_path(area_part_2)}")
