# --- Day 6: Universal Orbit Map ---
# Part 2 -

from networkx import Graph
from networkx.algorithms.shortest_paths import shortest_path_length


graph = Graph()

with open('./input.txt') as fp:
    orbits = {x[1]: x[0]
              for x in [x.split(')') for x in fp.read().split('\n') if x]}

for outer, inner in orbits.items():
    if not outer in graph:
        graph.add_node(outer)
    if not inner in graph:
        graph.add_node(inner)
    graph.add_edge(outer, inner)

print(shortest_path_length(graph, orbits['YOU'], orbits['SAN']))
