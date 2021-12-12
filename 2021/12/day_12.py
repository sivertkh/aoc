# --- Day 12: Passage Pathing ---

import networkx as nx


def generate_part_1_paths(graph, cur_path):
    res = []
    for a in graph.adj[cur_path[-1]]:
        if a.islower() and a in cur_path:
            continue
        p = cur_path + [a]
        if a == 'end':
            res.append(p)
            continue
        res.extend(generate_part_1_paths(graph, p))
    return res


def generate_part_2_paths(graph, cur_path, used_small=False):
    res = []
    for a in graph.adj[cur_path[-1]]:
        if a == 'start':
            continue
        local_used_small = used_small
        if a.islower() and a in cur_path:
            if used_small:
                continue
            local_used_small = True
        p = cur_path + [a]
        if a == 'end':
            res.append(p)
            continue
        res.extend(generate_part_2_paths(graph, p, used_small=local_used_small))
    return res


with open("input.txt") as fp:
    G = nx.Graph([[y for y in x.strip().split('-')] for x in fp.readlines()])

print(f"Part 1: {len(generate_part_1_paths(G, ['start']))}")
print(f"Part 2: {len(generate_part_2_paths(G, ['start']))}")
