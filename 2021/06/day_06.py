# --- Day 6: Lanternfish ---

with open("input.txt") as fp:
    numbers = fp.readline().strip().split(',')
    numbers = list(map(int, numbers))

fish = [0 for _ in range(9)]
for i in numbers:
    fish[i] += 1

for day in range(256):
    fish = fish[1:] + fish[:1]
    fish[-3] += fish[-1]
    if day == 80 - 1:
        print(f"Part 1: {sum(fish)}")

print(f"Part 2: {sum(fish)}")
