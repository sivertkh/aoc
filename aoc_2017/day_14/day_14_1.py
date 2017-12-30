# --- Day 14: Disk Defragmentation ---
# part 1 - ok

from aoc_2017.day_10.day_10_2 import create_hash

data = 'vbqugkhl'

grid = []
for i in range(128):
    grid.append([int(x) for x in bin(int(create_hash("{}-{}".format(data, i)),
                                         16))[2:]])

s = 0
for line in grid:
    s += sum(line)

print(s)
