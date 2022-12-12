# --- Day 12: Hill Climbing Algorithm ---

import networkx as nx
from aocd.models import Puzzle


def height_as_int(height: str) -> int:
    match height:
        case "S":
            return 1
        case "E":
            return 26
        case _:
            return ord(height) - 96


def can_move_to(
    data: list[list[str]], start: list[int, int], to: list[int, int]
) -> bool:
    start_height = height_as_int(data[start[0]][start[1]])
    to_height = height_as_int(data[to[0]][to[1]])

    if 0 <= to_height - start_height <= 1 or to_height < start_height:
        return True

    return False


def create_graph(input_data: str) -> list[nx.Graph, str, str, list[str]]:
    G = nx.DiGraph()

    data = [list(x) for x in input_data.split("\n") if x]

    start = end = ""
    a_starts = []

    for i in range(len(data)):
        for j in range(len(data[0])):

            if data[i][j] == "E":
                end = f"{i},{j}"
                continue
            elif data[i][j] == "S":
                start = f"{i},{j}"

            if data[i][j] == "a":
                a_starts.append(f"{i},{j}")

            if i > 0 and can_move_to(data, [i, j], [i - 1, j]):
                G.add_edge(f"{i},{j}", f"{i-1},{j}")

            if j > 0 and can_move_to(data, [i, j], [i, j - 1]):
                G.add_edge(f"{i},{j}", f"{i},{j-1}")

            if i < len(data) - 1 and can_move_to(data, [i, j], [i + 1, j]):
                G.add_edge(f"{i},{j}", f"{i+1},{j}")

            if j < len(data[0]) - 1 and can_move_to(data, [i, j], [i, j + 1]):
                G.add_edge(f"{i},{j}", f"{i},{j+1}")

    return G, start, end, a_starts


def solve():
    puzzle = Puzzle(year=2022, day=12)
    G, start, end, a_starts = create_graph(puzzle.input_data)

    part_1 = nx.shortest_path_length(G, source=start, target=end)
    part_2 = []
    for x in a_starts:
        try:
            part_2.append(nx.shortest_path_length(G, source=x, target=end))
        except nx.NetworkXNoPath:
            pass

    # puzzle.answer_a = part_1
    # puzzle.answer_b = min(part_2)

    return part_1, min(part_2)


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")


assert part_1 == 408
assert part_2 == 399
