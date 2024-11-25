# AOC 2023
# --- Day 16: The Floor Will Be Lava ---

from collections import deque
from enum import Enum

import networkx as nx


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def beam_path_length(
    data: list, start_x: int, start_y: int, start_direction: Direction
) -> int:
    G = nx.DiGraph()

    # Beam [x, y, direction]
    current_beams = deque()
    current_beams.append([start_x, start_y, start_direction])

    while current_beams:
        x, y, d = current_beams.popleft()

        match data[x][y]:
            case ".":
                # We continue in the current direction
                match d:
                    case Direction.UP:
                        if x - 1 >= 0 and not G.has_edge(f"{x},{y}", f"{x - 1},{y}"):
                            current_beams.append([x - 1, y, d])
                            G.add_edge(f"{x},{y}", f"{x - 1},{y}")
                    case Direction.DOWN:
                        if x + 1 < len(data) and not G.has_edge(
                            f"{x},{y}", f"{x + 1},{y}"
                        ):
                            current_beams.append([x + 1, y, d])
                            G.add_edge(f"{x},{y}", f"{x + 1},{y}")
                    case Direction.LEFT:
                        if y - 1 >= 0 and not G.has_edge(f"{x},{y}", f"{x},{y - 1}"):
                            current_beams.append([x, y - 1, d])
                            G.add_edge(f"{x},{y}", f"{x},{y - 1}")
                    case Direction.RIGHT:
                        if y + 1 < len(data[0]) and not G.has_edge(
                            f"{x},{y}", f"{x},{y + 1}"
                        ):
                            current_beams.append([x, y + 1, d])
                            G.add_edge(f"{x},{y}", f"{x},{y + 1}")
            case "/":
                match d:
                    case Direction.UP:
                        # Moving upwards. Changing direction to right.
                        if y + 1 < len(data[0]) and not G.has_edge(
                            f"{x},{y}", f"{x},{y + 1}"
                        ):
                            current_beams.append([x, y + 1, Direction.RIGHT])
                            G.add_edge(f"{x},{y}", f"{x},{y + 1}")
                    case Direction.DOWN:
                        # Moving downwards. Changing direction to left.
                        if y - 1 >= 0 and not G.has_edge(f"{x},{y}", f"{x},{y - 1}"):
                            current_beams.append([x, y - 1, Direction.LEFT])
                            G.add_edge(f"{x},{y}", f"{x},{y - 1}")
                    case Direction.LEFT:
                        # Moving leftwards. Changing direction to Down
                        if x + 1 < len(data) and not G.has_edge(
                            f"{x},{y}", f"{x + 1},{y}"
                        ):
                            current_beams.append([x + 1, y, Direction.DOWN])
                            G.add_edge(f"{x},{y}", f"{x + 1},{y}")
                    case Direction.RIGHT:
                        # Moving rightwards. Changing direction to up
                        if x - 1 >= 0 and not G.has_edge(f"{x},{y}", f"{x - 1},{y}"):
                            current_beams.append([x - 1, y, Direction.UP])
                            G.add_edge(f"{x},{y}", f"{x - 1},{y}")
            case "\\":
                match d:
                    case Direction.UP:
                        # Moving upwards. Changing direction to left.
                        if y - 1 >= 0 and not G.has_edge(f"{x},{y}", f"{x},{y - 1}"):
                            current_beams.append([x, y - 1, Direction.LEFT])
                            G.add_edge(f"{x},{y}", f"{x},{y - 1}")
                    case Direction.DOWN:
                        # Moving downwards. Changing direction to right.
                        if y + 1 < len(data[0]) and not G.has_edge(
                            f"{x},{y}", f"{x},{y + 1}"
                        ):
                            current_beams.append([x, y + 1, Direction.RIGHT])
                            G.add_edge(f"{x},{y}", f"{x},{y + 1}")
                    case Direction.LEFT:
                        # Moving leftwards. Changing direction to UP
                        if x - 1 >= 0 and not G.has_edge(f"{x},{y}", f"{x - 1},{y}"):
                            current_beams.append([x - 1, y, Direction.UP])
                            G.add_edge(f"{x},{y}", f"{x - 1},{y}")
                    case Direction.RIGHT:
                        # Moving rightwards. Changing direction to Down
                        if x + 1 < len(data) and not G.has_edge(
                            f"{x},{y}", f"{x + 1},{y}"
                        ):
                            current_beams.append([x + 1, y, Direction.DOWN])
                            G.add_edge(f"{x},{y}", f"{x + 1},{y}")
            case "-":
                match d:
                    case Direction.UP | Direction.DOWN:
                        # Split into left and right beam
                        if y - 1 >= 0 and not G.has_edge(f"{x},{y}", f"{x},{y - 1}"):
                            current_beams.append([x, y - 1, Direction.LEFT])
                            G.add_edge(f"{x},{y}", f"{x},{y - 1}")
                        if y + 1 < len(data[0]) and not G.has_edge(
                            f"{x},{y}", f"{x},{y + 1}"
                        ):
                            current_beams.append([x, y + 1, Direction.RIGHT])
                            G.add_edge(f"{x},{y}", f"{x},{y + 1}")
                    case Direction.LEFT:
                        # Continue straight through
                        if y - 1 >= 0 and not G.has_edge(f"{x},{y}", f"{x},{y - 1}"):
                            current_beams.append([x, y - 1, d])
                            G.add_edge(f"{x},{y}", f"{x},{y - 1}")
                    case Direction.RIGHT:
                        # Continue straight through
                        if y + 1 < len(data[0]) and not G.has_edge(
                            f"{x},{y}", f"{x},{y + 1}"
                        ):
                            current_beams.append([x, y + 1, d])
                            G.add_edge(f"{x},{y}", f"{x},{y + 1}")
            case "|":
                match d:
                    case Direction.UP:
                        # Continue straight through
                        if x - 1 >= 0 and not G.has_edge(f"{x},{y}", f"{x - 1},{y}"):
                            current_beams.append([x - 1, y, d])
                            G.add_edge(f"{x},{y}", f"{x - 1},{y}")
                    case Direction.DOWN:
                        # Continue straight through
                        if x + 1 < len(data) and not G.has_edge(
                            f"{x},{y}", f"{x + 1},{y}"
                        ):
                            current_beams.append([x + 1, y, d])
                            G.add_edge(f"{x},{y}", f"{x + 1},{y}")
                    case Direction.LEFT | Direction.RIGHT:
                        # Split into up and down beam
                        if x - 1 >= 0 and not G.has_edge(f"{x},{y}", f"{x - 1},{y}"):
                            current_beams.append([x - 1, y, Direction.UP])
                            G.add_edge(f"{x},{y}", f"{x - 1},{y}")
                        if x + 1 < len(data) and not G.has_edge(
                            f"{x},{y}", f"{x + 1},{y}"
                        ):
                            current_beams.append([x + 1, y, Direction.DOWN])
                            G.add_edge(f"{x},{y}", f"{x + 1},{y}")

    return G.number_of_nodes()


def find_largest_beam_path(data: list) -> int:

    return max(
        [
            max(
                [
                    beam_path_length(data, 0, y, Direction.DOWN)
                    for y in range(len(data[0]))
                ]
            ),
            max(
                [
                    beam_path_length(data, len(data) - 1, y, Direction.UP)
                    for y in range(len(data[0]))
                ]
            ),
            max(
                [
                    beam_path_length(data, x, 0, Direction.RIGHT)
                    for x in range(len(data))
                ]
            ),
            max(
                [
                    beam_path_length(data, x, len(data[0]) - 1, Direction.LEFT)
                    for x in range(len(data))
                ]
            ),
        ]
    )


def solve():
    with open("input.txt", "r") as fp:
        data = [list(x.strip()) for x in fp.readlines() if x]
    return beam_path_length(data, 0, 0, Direction.RIGHT), find_largest_beam_path(data)


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 7482
assert part_2 == 7896
