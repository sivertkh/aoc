# --- Day 2: Dive! ---

with open("input.txt") as fp:
    moves = [x.strip().split() for x in fp.readlines()]

horizontal = 0
aim = 0
depth = 0

for direction, stept in moves:
    step = int(stept)
    match direction:
        case "down":
            aim += step
        case "up":
            aim -= step
        case "forward":
            horizontal += step
            depth += aim * step

print(f"Part 1: {horizontal * aim}")
print(f"Part 2: {horizontal * depth}")
