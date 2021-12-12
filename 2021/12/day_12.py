# --- Day 12: Passage Pathing ---

import networkx as nx


def generate_paths(graph, cur_path, used_small=False):
    res_1 = []
    res_2 = []
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
            if not used_small:
                res_1.append(p)
            res_2.append(p)
            continue
        r1, r2 = generate_paths(graph, p, used_small=local_used_small)
        res_1 += r1
        res_2 += r2
    return res_1, res_2


with open("input.txt") as fp:
    G = nx.Graph([[y for y in x.strip().split('-')] for x in fp.readlines()])

r1, r2 = generate_paths(G, ['start'])
print(f"Part 1: {len(r1)}")
print(f"Part 2: {len(r2)}")
