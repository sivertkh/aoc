# --- Day 6: Memory Reallocation ---
# part 2 -

import numpy as np

with open('input.txt', 'r') as fp:
    banks = [int(x.rstrip()) for x in fp.read().split('\t')]
#banks = np.array([0, 2, 7, 0])

known_states = {}
print(",".join([str(x) for x in banks]))
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

    # Save new state
    state = ",".join([str(x) for x in banks])
    print(state)

    if state in known_states:
        print("Found the same config after {}".format(len(known_states)+1))

        start = known_states[state]
        end = len(known_states) + 1

        print("size of loop: {}".format((end - start)))
        exit(0)
    else:
        known_states[state] = len(known_states)+1
