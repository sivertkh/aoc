# --- Day 6: Memory Reallocation ---
# Part 1 - ok

import numpy as np

with open('input.txt', 'r') as fp:
    banks = [int(x.rstrip()) for x in fp.read().split('\t')]

known_states = set()
while True:
    mx = np.argmax(banks)
    dist = banks[mx]
    banks[mx] = 0
    pos = mx

    while dist > 0:
        pos = pos + 1
        if pos > len(banks) - 1:
            # At the end
            pos = 0

        banks[pos] = banks[pos] + 1
        dist = dist - 1

    state = ",".join([str(x) for x in banks])

    if state in known_states:
        print("Found the same config after {} cycles".format(len(known_states)+1))
        exit(0)
    else:
        known_states.add(state)
