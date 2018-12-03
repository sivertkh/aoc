# --- Day 7: Recursive Circus ---
# Part 1 -

from collections import deque


class Node:
    def __init__(self, name, weight, edges):
        self.name = name
        self.weight = weight
        self.edges = edges

    def __str__(self):
        return "{} {}".format(self.name, self.edges)


def create_tree():
    nodes = {}
    with open('input.txt', 'r') as fp:
        for line in fp:
            n = line.rstrip().split(" ")
            if len(n) > 2:
                edges = [x.rstrip(',') for x in n[3:]]
                nodes[n[0]] = Node(n[0], n[1], edges)
            else:
                # simple node
                nodes[n[0]] = Node(n[0], n[1], None)

    # The root needs to have edges
    ed = [v for k, v in nodes.items() if v.edges is not None]

    root = None
    edges = [x.edges for x in ed]

    def flatten(l): return [item for sublist in l for item in sublist]

    edges = flatten(edges)

    for n in ed:
        if n.name not in edges:
            root = n.name
    return root


if __name__ == "__main__":
    print(create_tree())
