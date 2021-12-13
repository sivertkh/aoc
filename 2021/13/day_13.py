# --- Day 13: Transparent Origami ---

import numpy as np

with open("input.txt") as fp:
    start, folds = fp.read().strip().split("\n\n")

start = [[int(y) for y in x.split(",")] for x in start.split("\n")]
folds = [x.split()[-1] for x in folds.split("\n")]
folds = [x.split("=") for x in folds]
max_x = max([x[0] for x in start])
max_y = max([x[1] for x in start])

paper = np.array([["." for _ in range(max_x + 1)] for _ in range(max_y + 1)])
for x, y in start:
    paper[y][x] = "#"

first = True
for axis, line in folds:
    line = int(line)
    if axis == "x":
        left = paper[0:, 0:line].copy()
        right = paper[0:, line + 1 :].copy()
        right = np.flip(right, axis=1)
        for i in range(len(right)):
            for j in range(len(right[0])):
                if right[i][j] == "#":
                    left[i][j] = "#"
        paper = left

    else:
        top = paper[0:line].copy()
        bottom = paper[line + 1 :].copy()
        bottom = np.flip(bottom, axis=0)
        for i in range(len(bottom)):
            for j in range(len(bottom[0])):
                if bottom[i][j] == "#":
                    top[i][j] = "#"
        paper = top

    if first:
        part_1 = sum([sum([1 for y in x if y == "#"]) for x in paper])
        print(f"Part1: {part_1}")
        first = False

print("Part 2:")
for x in paper:
    print("".join(x).replace(".", " "))
