# AOC 2023
# --- Day 14: Parabolic Reflector Dish ---

from enum import Enum

import numpy as np


class Direction(Enum):
    NORTH = 1
    WEST = 2
    SOUTH = 3
    EAST = 4


def tilt(s: np.array, direction: Direction):
    # Flip or rotate
    match direction:
        case Direction.NORTH:
            # Do nothing
            pass
        case Direction.WEST:
            s = np.rot90(s, 3)
        case Direction.SOUTH:
            s = np.flipud(s)
        case Direction.EAST:
            # TODO find a better way..
            s = np.rot90(s)

    for x in range(len(s)):
        for y in range(len(s[x])):
            if s[x][y] == "O":
                for pos in range(x - 1, -1, -1):
                    if s[pos][y] != ".":
                        # Found where to stop..
                        s[x][y] = "."
                        s[pos + 1][y] = "O"
                        break
                    elif pos == 0:
                        s[x][y] = "."
                        s[0][y] = "O"
                        break

    # Flip and rotate array back
    match direction:
        case Direction.NORTH:
            # Do nothing
            pass
        case Direction.WEST:
            s = np.rot90(s)
        case Direction.SOUTH:
            s = np.flipud(s)
        case Direction.EAST:
            s = np.rot90(s, 3)

    return s


def solve_part_1(s: np.array) -> int:
    s = tilt(s, Direction.NORTH)
    return sum([np.count_nonzero(x == "O") * (len(s) - i) for i, x in enumerate(s)])


def solve_part_2(s: np.array) -> int:

    lookup_table = []

    nr_cycles = 1000000000
    for x in range(1, nr_cycles + 1):
        for d in [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST]:
            s = tilt(s, d)

        pos = []
        for i in s:
            pos.append(",".join([str(k) for k in list(np.where(i == "O")[0])]))
        pos = ";".join(pos)

        if pos in lookup_table:
            print(f"Found loop after {x} circles!")
            lookup_table.append(pos)
            break

        lookup_table.append(pos)

    loop_start = lookup_table.index(lookup_table[-1])
    loop_length = len(lookup_table) - loop_start - 1
    pre_loop_length = len(lookup_table) - loop_length - 1
    cycle_position = (nr_cycles - pre_loop_length - 1) % loop_length

    res = 0
    for i, x in enumerate(
        lookup_table[pre_loop_length + cycle_position].split(";")[::-1]
    ):
        if x:
            res += (i + 1) * len(x.split(","))

    return res


def solve():
    with open("input.txt", encoding="utf8") as fp:
        s = np.array([list(x) for x in fp.read().split("\n") if x])
    return solve_part_1(s), solve_part_2(s)


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 110821
assert part_2 == 83516
