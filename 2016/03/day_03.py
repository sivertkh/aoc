# --- Day 3: Squares With Three Sides ---

import itertools
import numpy as np


def possible_triangles(triangles):
    return len(triangles) - len([y for y in [[x for x in itertools.permutations(t, 3) if sum(x[:-1]) <= x[-1]] for t in triangles] if y])


with open('./input.txt') as fp:
    triangles = np.array([list(map(int, x.rstrip().split())) for x in fp.readlines()])

print(f'Part 1: {possible_triangles(triangles)}')

triangles = np.reshape(np.transpose(triangles), triangles.shape)
print(f'Part 2: {possible_triangles(triangles)}')
