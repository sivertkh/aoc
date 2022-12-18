# --- Day 18: Boiling Boulders ---

import numpy as np
from scipy import ndimage

from aocd.models import Puzzle


def surface_area(grid: np.array) -> int:
    return sum(
        [
            6
            - np.sum(
                [
                    grid[x + 1, y, z],
                    grid[x - 1, y, z],
                    grid[x, y + 1, z],
                    grid[x, y - 1, z],
                    grid[x, y, z + 1],
                    grid[x, y, z - 1],
                ],
                dtype=int,
            )
            for x, y, z in zip(*np.where(grid == 1))
        ]
    )


def solve():
    puzzle = Puzzle(year=2022, day=18)
    part_1 = part_2 = 0

    cubes = np.array(
        [list(map(int, x.split(","))) for x in puzzle.input_data.split("\n")]
    )
    grid = np.zeros([max(cubes[:, i]) + 2 for i in range(3)])
    for x, y, z in cubes:
        grid[x, y, z] = 1

    part_1 = surface_area(grid)
    grid = ndimage.binary_fill_holes(grid).astype(int)
    part_2 = surface_area(grid)

    # puzzle.answer_a = part_1
    # puzzle.answer_b = part_2
    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 4444
assert part_2 == 2530
