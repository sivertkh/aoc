# --- Day 1: Sonar Sweep ---

with open("input.txt") as fp:
    depths = [int(x.strip()) for x in fp.readlines()]

part_1 = sum(map(lambda a, b: 1 if b > a else 0, depths[:-1], depths[1:]))
depths = list(zip(depths[:-2], depths[1:-1], depths[2:]))
part_2 = sum(map(lambda a, b: 1 if sum(b) > sum(a) else 0, depths[:-1], depths[1:]))

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
