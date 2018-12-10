#
# Part 1 -

import re

with open('simple.txt') as fp:

    data = [x for x in fp.read().split('\n') if x]
    pos = []
    for d in data:
        m = re.search(
            "position=<(\-*\s*\d*), (\-*\s*\d*)> velocity=<(\-*\s*\d*), (\-*\s*\d*)>",
            d)
        # <X, Y> <X_change, Y_change>
        pos.append([int(m[1]), int(m[2]), int(m[3]), int(m[4])])

last = 0
for i in range(20):
    for p in pos:
        p[0] += p[2]
        p[1] += p[3]

    max_x = max([p[0] for p in pos])
    min_x = min([p[0] for p in pos])
    max_y = max([p[1] for p in pos])
    min_y = min([p[1] for p in pos])
    box = max_x - min_y * max_y - min_y

    if last < box:
        p[0] -= p[2]
        p[1] -= p[3]

        exit()

    last = box
    print(box)
