# --- Day 18: Settlers of The North Pole ---
# Part 1 - ok

import copy
import numpy as np

with open('input.txt') as fp:
    area = np.array([list(x) for x in fp.read().split('\n') if x])

length = 10
for m in range(1, 10+1):

    tmp = area.copy()
    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            adjacent = []
            if i == 0 and j == 0:
                adjacent = tmp[:2, :2]
            elif i == len(tmp) - 1 and j == len(tmp[0]) - 1:
                adjacent = tmp[-2:, -2:]
            elif i == 0:
                adjacent = tmp[0:2:, j-1:j+2]
            elif j == 0:
                adjacent = tmp[i-1:i+2:, 0:2]
            elif i == len(tmp) - 1:
                adjacent = tmp[-2:, j-1:j+2]
            elif j == len(tmp[0]) - 1:
                adjacent = tmp[i-1:i+2, -2:]
            else:
                adjacent = tmp[i-1:i+2, j-1:j+2:]

            # Flatten
            adjacent = [item for sublist in adjacent for item in sublist]

            if tmp[i][j] == '#':
                if sum([1 for x in adjacent if x == '#']) > 1 and sum([1 for x in adjacent if x == '|']) >= 1:
                    area[i][j] = '#'
                else:
                    area[i][j] = '.'
            elif tmp[i][j] == '|':
                if sum([1 for x in adjacent if x == '#']) >= 3:
                    area[i][j] = '#'
            else:
                if sum([1 for x in adjacent if x == '|']) >= 3:
                    area[i][j] = '|'

woods = sum([sum([1 for x in y if x == '|']) for y in area])
yards = sum([sum([1 for x in y if x == '#']) for y in area])
print(woods * yards)
