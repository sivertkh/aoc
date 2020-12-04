# --- Day 3: Toboggan Trajectory ---
from functools import reduce


with open('./input.txt') as fp:
    m = [list(x.rstrip()) for x in fp.readlines()]

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
positions = [list(zip(range(x[1], len(m), x[1]), range(x[0], (len(m)//x[1])*x[0]+1, x[0]))) for x in slopes]
hits = [sum([m[y[0]][y[1] % len(m[0])] == "#" for y in x]) for x in positions]

print(f'Part 1: {hits[1]}')
print(f'Part 2: {reduce(lambda x ,y: x*y, hits)}')
