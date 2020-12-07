# --- Day 7: Handy Haversacks ---
import re
from collections import deque

import networkx as nx
from networkx.algorithms.traversal.breadth_first_search import bfs_tree

nodes = {}

with open('./input.txt') as fp:
    for rule in fp.readlines():
        r = re.sub(r'bags|bag', '', rule.rstrip()).replace('.', '').split(' contain ')
        nodes[r[0].strip()] = [list(re.match('(\d*) ([\w\s]*)', x).groups()) for x in r[1].split(', ') if 'no other' not in x ]

graph = nx.DiGraph()
for node, edges in nodes.items():
    for e in edges:
        graph.add_edge(e[1].strip(), node, weight=int(e[0]))

print(f'Part 1: {len(bfs_tree(graph, "shiny gold"))-1}')


def bag_weight(node):
    if not graph.in_edges(node):
        return 1
    return sum([bag_weight(edge[0]) * edge[2]['weight'] for edge in graph.in_edges(node, data=True)]) + 1


print(f'Part 2: {bag_weight("shiny gold") - 1}')