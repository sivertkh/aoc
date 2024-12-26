# AOC 2024
# --- Day 18: RAM Run ---

import networkx as nx


def create_graph(data: list, steps: int) -> nx.Graph:
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
    return G


def solve_part_1(data: list) -> int:
    G = create_graph(data, steps=1024)
    return nx.shortest_path_length(G, (0, 0), (70, 70))


def find_shortest_no_path(data: list, steps_start: int, steps_end: int) -> str:
    steps = (steps_start + steps_end) // 2

    if steps == steps_start:
        y, x = data[steps_start]
        return f"{y},{x}"

    G = create_graph(data, steps=steps)
    if nx.has_path(G, (0, 0), (70, 70)):
        return find_shortest_no_path(data, steps, steps_end)

    return find_shortest_no_path(data, steps_start, steps)


def solve_part_2(data: list) -> str:
    return find_shortest_no_path(data, 0, len(data) - 1)


def solve() -> tuple[int, str]:
    with open("input.txt", encoding="utf-8") as fp:
        data = [list(map(int, x.split(","))) for x in fp.read().split("\n") if x]
    return solve_part_1(data), solve_part_2(data)


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
    assert part_1 == 416
    assert part_2 == "50,23"
