# --- Day 2: Dive! ---

with open("input.txt") as fp:
    moves = [x.strip().split() for x in fp.readlines()]

horizontal = 0
depth_part_1 = 0

aim = 0
depth_part_2 = 0

for move in moves:

    match move[0]:
        case "down":
            depth_part_1 += int(move[1])
            aim += int(move[1])
        case "up":
            depth_part_1 -= int(move[1])
            aim -= int(move[1])
        case "forward":
            horizontal += int(move[1])
            depth_part_2 += aim * int(move[1])

print(f"Part 1: {horizontal * depth_part_1}")
print(f"Part 2: {horizontal * depth_part_2}")
