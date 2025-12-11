"""
AOC 2025
--- Day 11: Reactor ---
"""

import networkx as nx


def solve_part_1(G, source, target):
    memo = {}

    def dfs(node):
        if node == target:
            return 1
        if node in memo:
            return memo[node]

        count = sum(dfs(successor) for successor in G.successors(node))
        memo[node] = count
        return count

    return dfs(source)


def solve_part_2(G, source, target, required_nodes):
    memo = {}

    def dfs(current, idx):
        if idx == len(required_nodes) and current == target:
            return 1

        key = (current, idx)
        if key in memo:
            return memo[key]

        if idx < len(required_nodes) and current == required_nodes[idx]:
            idx += 1

        count = sum(dfs(next_node, idx) for next_node in G.successors(current))

        memo[key] = count
        return count

    return dfs(source, 0)


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        data = [x.split() for x in fp.read().split("\n") if x]

    G = nx.DiGraph()
    for x in data:
        start = x[0].strip(":")
        G.add_edges_from([(start, dest) for dest in x[1:]])

    assert nx.is_directed_acyclic_graph(G)

    # As the graph is a DAG, we can only pass through the required nodes in one ordering.
    # For my input, this is fft first, then dac. This my not be true for other inputs.
    return solve_part_1(G, "you", "out"), solve_part_2(G, "svr", "out", ["fft", "dac"])


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

    assert part_1 == 603
    assert part_2 == 380961604031372
