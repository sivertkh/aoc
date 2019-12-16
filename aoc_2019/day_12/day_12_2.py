# --- Day 12: The N-Body Problem ---
# Part 1 -

import itertools

with open('simple.txt') as fp:
    moons = [x.split(',') for x in fp.read().split('\n') if x]
    moons = [[int(x.split('=')[-1].replace('>', ''))
              for x in moon] for moon in moons]

moons_v = [[0 for _ in range(3)] for _ in range(len(moons))]

moons_origin = moons.copy()
moons_v_origin = moons_v.copy()

steps = 0
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
    steps += 1

    if

    for i in range(len(moons)):
        if not moons[i] == moons_origin[i] and moons_v[i] == moons_v_origin[i]:
            break
    else:
        break

print(steps)


# for i in range(len(moons)):
#    m = moons[i]
#    v = moons_v[i]
#    print(
#        f'pos=<x={m[0]:3}, y={m[1]:3}, z={m[2]:3}>, vel=<x={v[0]:3}, y={v[1]:3}, z={v[2]:3}>')
#
#energy = 0
#
# for i in range(len(moons)):
#
#    energy += sum(abs(x) for x in moons[i]) * sum(abs(x) for x in moons_v[i])
#
# print(energy)
#
