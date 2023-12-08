# AOC 2023
# --- Day 8: Haunted Wasteland ---

import math


def find_path_len(path, graph, start="AAA", part_2=False):
    steps = 0
    cur_pos = start
    cur_direction = path[0]
    while True:
        cur_pos = graph[cur_pos][cur_direction]
        steps += 1
        if (not part_2 and cur_pos == "ZZZ") or (part_2 and cur_pos[-1] == "Z"):
            break
        cur_direction = path[steps % len(path)]
    return steps


def solve():
    part_1 = 0
    part_2 = 0

    with open("input.txt") as fp:
        s = fp.read()

    path, graph_data = s.split("\n\n")

    path = list(path.strip())
    graph = {}
    part_2_starts = []
    for x in [x.strip() for x in graph_data.split("\n") if x]:
        name, next = x.split(" = ")
        left, right = next[1:-1].split(", ")
        graph[name] = {"L": left, "R": right}
        if name[-1] == "A":
            part_2_starts.append(name)

    part_1 = find_path_len(path, graph)
    part_2 = math.lcm(
        *[find_path_len(path, graph, start=x, part_2=True) for x in part_2_starts]
    )

    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 12643
assert part_2 == 13133452426987
