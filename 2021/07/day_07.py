# --- Day 7: The Treachery of Whales ---

with open("input.txt") as fp:
    numbers = list(map(int, fp.readline().strip().split(",")))

part_1_min = None
part_2_min = None

for i in range(min(numbers), max(numbers)):
    part_1 = [abs(x - i) for x in numbers]
    part_2 = [(abs(x - i) * (abs(x - i) + 1) // 2) for x in numbers]

    if not part_1_min or sum(part_1) < part_1_min:
        part_1_min = sum(part_1)
    if not part_2_min or sum(part_2) < part_2_min:
        part_2_min = sum(part_2)

print(f"Part 1: {part_1_min}")
print(f"Part 2: {part_2_min}")
