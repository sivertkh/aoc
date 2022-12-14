# --- Day 14: Regolith Reservoir ---

import copy
from aocd.models import Puzzle


def find_sand_pos(cave_map, max_y, sand_x, sand_y):
    first_position = -1
    for y in range(sand_y, max_y):
        if cave_map[y + 1][sand_x] != ".":
            first_position = y
            break

    if first_position == -1:
        raise Exception()

    if all([x != "." for x in cave_map[first_position + 1][sand_x - 1 : sand_x + 2]]):
        return first_position, sand_x
    else:
        if cave_map[first_position + 1][sand_x - 1] == ".":
            return find_sand_pos(cave_map, max_y, sand_x - 1, first_position)
        elif cave_map[first_position + 1][sand_x + 1] == ".":
            return find_sand_pos(cave_map, max_y, sand_x + 1, first_position)
        else:
            raise Exception("Should never happen!")


def solve():
    puzzle = Puzzle(year=2022, day=14)
    part_1 = part_2 = 0
    data = [
        [list(map(int, y.split(","))) for y in x.split(" -> ")]
        for x in puzzle.input_data.split("\n")
        if x
    ]

    max_y = max([max([b[1] for b in a]) for a in data])

    # Adjust the start to optimize array size
    sand_x = max_y + 2
    x_adjust = 500 - sand_x

    cave_map_part_1 = [["." for _ in range((sand_x * 2) + 1)] for _ in range(max_y + 3)]

    for l in data:
        for i in range(len(l) - 1):
            start_x, start_y = l[i]
            end_x, end_y = l[i + 1]
            start_x -= x_adjust
            end_x -= x_adjust

            if start_x == end_x:
                for y in (
                    range(start_y, end_y + 1)
                    if start_y < end_y
                    else range(end_y, start_y + 1)
                ):
                    cave_map_part_1[y][start_x] = "#"

            else:
                for x in (
                    range(start_x, end_x + 1)
                    if start_x < end_x
                    else range(end_x, start_x + 1)
                ):
                    cave_map_part_1[start_y][x] = "#"

    cave_map_part_2 = copy.deepcopy(cave_map_part_1)
    for x in range(0, len(cave_map_part_2[0])):
        cave_map_part_2[max_y + 2][x] = "#"

    while True:
        try:
            y, x = find_sand_pos(cave_map_part_1, max_y + 2, sand_x, 0)
            cave_map_part_1[y][x] = "o"
        except Exception:
            part_1 = sum(
                [sum([1 if x == "o" else 0 for x in y]) for y in cave_map_part_1]
            )
            break

    while True:
        y, x = find_sand_pos(cave_map_part_2, max_y + 2, sand_x, 0)
        cave_map_part_2[y][x] = "o"

        if y == 0 and x == sand_x:
            part_2 = sum(
                [sum([1 if x == "o" else 0 for x in y]) for y in cave_map_part_2]
            )
            break

    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 817
assert part_2 == 23416
