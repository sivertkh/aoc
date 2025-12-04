"""
AOC 2025
--- Day 4: Printing Department ---
"""

import numpy as np


def removable_rols(m: np.ndarray) -> list[tuple[int, int]]:
    forklifts = []

    rol_positions = set(zip(*np.where(m == "@")))

    neighbour_pos = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]

    for x, y in rol_positions:
        neighbours = 0
        for dx, dy in neighbour_pos:
            if (x + dx, y + dy) in rol_positions:
                neighbours += 1

        if neighbours < 4:
            forklifts.append((x, y))

    return forklifts


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        m = np.array([list(x) for x in fp.read().split("\n") if x])

    part_1_res = len(removable_rols(m))

    removed = 0
    while len(rols := removable_rols(m)) != 0:
        removed += len(rols)
        for x, y in rols:
            m[x, y] = "."

    return part_1_res, removed


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

    assert part_1 == 1433
    assert part_2 == 8616
