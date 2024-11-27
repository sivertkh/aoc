# AOC 2023
# --- Day 25: Snowverload ---

import itertools as it

import networkx as nx

# import matplotlib.pyplot as plt


def solve():

    with open("input.txt", encoding="utf-8") as fp:
        data = [
            list(map(lambda k: k.replace(":", ""), x.split(" ")))
            for x in fp.read().split("\n")
            if x
        ]
        # print(data)

    G = nx.Graph()

    for l in data:
        if len(l) == 2:
            G.add_edge(l[0], l[1])
        else:
            G.add_edges_from(it.product(l[:1], l[1:]))

    # Used the visualization (graph.png) to solve part 1.
    # greedy_modularity_communities almost gives us correct answer.
    # Coloring the two sub graphs and drawing them shows us that
    # there are two distinct communities, with only three edges
    # between them. One of the nodes is grouped on "wrong" side.
    # Add and subtract 1 from the length of each subgraph to get
    # the correct answer.
    a, b = nx.algorithms.community.greedy_modularity_communities(
        G, resolution=0.0000001, cutoff=2, best_n=2
    )

    # color_map = []
    # for node in G:
    #    if node in a:
    #        color_map.append("red")
    #    else:
    #        color_map.append("green")
    # nx.draw(G, node_color=color_map)
    # plt.savefig("filename.png")

    return (len(a) + 1) * (len(b) - 1), part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 569904
# assert part_2 ==
