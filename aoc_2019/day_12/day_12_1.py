# --- Day 12: The N-Body Problem ---
# Part 1 -

import itertools

with open('input.txt') as fp:
    moons = [x.split(',') for x in fp.read().split('\n') if x]
    moons = [[int(x.split('=')[-1].replace('>', ''))
              for x in moon] for moon in moons]

moons_v = [[0 for _ in range(3)] for _ in range(len(moons))]

for step in range(1000):
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

energy = 0
for i in range(len(moons)):
    energy += sum(abs(x) for x in moons[i]) * sum(abs(x) for x in moons_v[i])
print(energy)
