# --- Day 14: Disk Defragmentation ---
# part 1 - ok

from aoc_2017.day_10.day_10_2 import create_hash

data = 'vbqugkhl'
#data = 'flqrgnkx'

grid = []
for i in range(128):
    tmp = [x for x in create_hash("{}-{}".format(data, i))]
    tmp2 = [bin(int(x, 16))[2:].rjust(4, "0") for x in tmp]
    grid.append([int(item) for sublist in tmp2 for item in sublist])

s = 0
for line in grid:
    s += sum(line)

print(s)

