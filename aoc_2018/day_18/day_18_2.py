# --- Day 18: Settlers of The North Pole ---
# Part 2 - 

import copy
import numpy as np

with open('input.txt') as fp:
    area = np.array([list(x) for x in fp.read().split('\n') if x])

length = 1000000000
seen = {}

values = {}

circle_start = 0
circle_end = 0

for m in range(0, length+1):

    s = ''.join([''.join(x) for x in area])

    woods = sum([sum([1 for x in y if x == '|']) for y in area])
    yards = sum([sum([1 for x in y if x == '#']) for y in area])

    values[m] = woods * yards

    if s in seen:
        circle_start = seen[s]
        circle_end = m
        break 

    seen[s] = m
    
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


# first circle at circle start
length = length - circle_start

circle_length = circle_end - circle_start 
rest = circle_start + (length % circle_length)

print(f'{values[rest]}')

