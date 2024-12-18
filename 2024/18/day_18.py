# AOC 2024
# --- Day 18: RAM Run ---

import networkx as nx


def shortest_path_length(data, steps):
    memory = [["." for _ in range(71)] for _ in range(71)]

    for i in range(steps):
        y, x = data[i]
        memory[x][y] = "#"

    edges = []
    # pylint: disable=C0200
    for x in range(len(memory)):
        for y in range(len(memory[0])):
            if memory[x][y] != "#":
                if x > 0 and memory[x - 1][y] != "#":
                    edges.append(((x, y), (x - 1, y)))
                if x < len(memory) - 1 and memory[x + 1][y] != "#":
                    edges.append(((x, y), (x + 1, y)))
                if y > 0 and memory[x][y - 1] != "#":
                    edges.append(((x, y), (x, y - 1)))
                if y < len(memory[0]) - 1 and memory[x][y + 1] != "#":
                    edges.append(((x, y), (x, y + 1)))

    G = nx.Graph()
    G.add_edges_from(edges)
    return nx.shortest_path_length(G, (0, 0), (len(memory) - 1, len(memory[0]) - 1))


def solve_part_1(data):
    return shortest_path_length(data, steps=1024)


def find_shortest_no_path(data, steps_start, steps_end):
    steps = (steps_start + steps_end) // 2

    if steps == steps_start:
        y, x = data[steps_start]
        return f"{y},{x}"
    try:
        shortest_path_length(data, steps=steps)
    except nx.NetworkXNoPath:
        # No path. ans is between new_start and i_new
        return find_shortest_no_path(data, steps_start, steps)
    else:
        # Found path, ans is between new_i and i_end
        return find_shortest_no_path(data, steps, steps_end)


def solve_part_2(data):
    return find_shortest_no_path(data, 0, len(data) - 1)


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        data = [list(map(int, x.split(","))) for x in fp.read().split("\n") if x]
    return solve_part_1(data), solve_part_2(data)


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 416
assert part_2 == "50,23"
