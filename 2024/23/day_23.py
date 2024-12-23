# AOC 2024
# --- Day 23: LAN Party ---

import itertools as it
import networkx as nx


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        data = [tuple(x.split("-")) for x in fp.read().split("\n") if x]

    G = nx.Graph()
    G.add_edges_from(data)

    max_clique = []
    cliques_3 = set()

    for clique in nx.algorithms.clique.find_cliques(G):
        if len(clique) >= 3:
            for sub_clique in it.combinations(clique, 3):
                if any((t[0] == "t" for t in sub_clique)):
                    sub_clique = list(sub_clique)
                    sub_clique.sort()
                    cliques_3.add(tuple(sub_clique))

        if len(clique) > len(max_clique):
            max_clique = clique

    max_clique.sort()
    return len(cliques_3), ",".join(max_clique)


if __name__ == "__main":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
    assert part_1 == 1218
    assert part_2 == "ah,ap,ek,fj,fr,jt,ka,ln,me,mp,qa,ql,zg"
