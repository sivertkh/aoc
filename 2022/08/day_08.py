# --- Day 7: No Space Left On Device ---

from aocd.models import Puzzle
import numpy as np


def solve():
    puzzle = Puzzle(year=2022, day=8)
    part_1 = part_2 = 0

    data = np.array([[int(y) for y in x] for x in puzzle.input_data.split("\n") if x])

    part_1 = len(data) * 2 + len(data[0]) * 2 - 4
    part_2 = None

    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            cur = data[i][j]

            row = data[:, j]
            column = data[i, :]
            left = column[:j]
            right = column[j + 1 :]
            up = row[:i]
            down = row[i + 1 :]

            if any([cur > x for x in [max(up), max(down), max(left), max(right)]]):
                part_1 += 1

            scenic_score = []
            for x in [np.flip(up), down, np.flip(left), right]:
                local_score = 0
                for l in range(len(x)):
                    if cur <= x[l]:
                        local_score = l + 1
                        break

                if local_score == 0:
                    # Look all the way to the edge
                    local_score = len(x)
                scenic_score.append(local_score)

            scenic_score = np.prod(scenic_score)
            if not part_2 or scenic_score > part_2:
                part_2 = scenic_score

    # puzzle.answer_a = part_1
    # puzzle.answer_b = part_2
    return part_1, part_2


part_1, part_2 = solve()
assert part_1 == 1776
assert part_2 == 234416
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
