# --- Day 10: The Stars Align ---
# Part 1 and 2 - ok

import re

with open('input.txt') as fp:

    data = [x for x in fp.read().split('\n') if x]
    pos = []
    for d in data:
        m = re.search(
            "position=<(\-*\s*\d*), (\-*\s*\d*)> velocity=<(\-*\s*\d*), (\-*\s*\d*)>",
            d)
        # <X, Y> <X_change, Y_change>
        pos.append([int(m[1]), int(m[2]), int(m[3]), int(m[4])])

last = None
for i in range(200000):
    for p in pos:
        p[0] += p[2]
        p[1] += p[3]

    max_x = max([p[0] for p in pos])
    min_x = min([p[0] for p in pos])
    max_y = max([p[1] for p in pos])
    min_y = min([p[1] for p in pos])
    box = abs(max_x - min_x) * abs(max_y - min_y)

    if last and last < box:

        print(f'At sec {i}')
        for p in pos:
            p[0] -= p[2]
            p[1] -= p[3]

        max_x = max([p[0] for p in pos])
        min_x = min([p[0] for p in pos])
        max_y = max([p[1] for p in pos])
        min_y = min([p[1] for p in pos])
        array = [['.' for x in range(max_x-min_x+1)] for y in range(max_y-min_y+1)]

        for p in pos:
            array[p[1]-min_y][p[0]-min_x] = '#' 

        for a in array:
            print(''.join(a))

        exit()

    last = box
