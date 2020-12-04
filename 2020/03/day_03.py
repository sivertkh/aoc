# --- Day 3: Toboggan Trajectory ---
from functools import reduce


with open('./input.txt') as fp:
    m = [list(x.rstrip()) for x in fp.readlines()]

res = [sum([1 for x in y if m[x[0]][x[1] % len(m[0])] == "#"]) for y in [list(zip(range(x[1], len(m), x[1]), range(x[0], (len(m)//x[1])*x[0]+1, x[0]))) for x in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]]]

print(f'Part 1: {res[1]}')
print(f'Part 2: {reduce(lambda x ,y: x*y, res)}')
