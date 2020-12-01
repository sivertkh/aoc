# --- Day 12: The N-Body Problem ---
# Part 2 - ok

import itertools
import math
from functools import reduce

with open('input.txt') as fp:
    moons = [x.split(',') for x in fp.read().split('\n') if x]
    moons = [[int(x.split('=')[-1].replace('>', ''))
              for x in moon] for moon in moons]

moons_v = [[0 for _ in range(3)] for _ in range(len(moons))]
start_axis = [[x[i] for x in moons] for i in range(3)]
step = 0
periods = [-1 for _ in range(3)]
while True:
    for a, b in itertools.permutations(range(len(moons)), 2):
        moon_a = moons[a]
        moon_b = moons[b]
        for axis in range(3):
            if moon_a[axis] < moon_b[axis]:
                moons_v[a][axis] += 1
                moons_v[b][axis] -= 1
            elif moon_a[axis] < moon_b[axis]:
                moons_v[a][axis] -= 1
                moons_v[b][axis] += 1

    for i in range(len(moons)):
        for axis in range(3):
            moons[i][axis] += moons_v[i][axis]
    step += 1

    for i in range(3):
        cur_i = [x[i] for x in moons]
        cur_v = [x[i] for x in moons_v]
        if periods[i] == -1 and all([v == 0 for v in cur_v]) and cur_i == start_axis[i]:
            periods[i] = step

    if all([x != -1 for x in periods]):
        break

print(reduce(lambda a, b: a*b//math.gcd(a, b), periods))
