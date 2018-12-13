# --- Day 12: Subterranean Sustainability ---
# Part 2 - ok

import numpy as np

with open('input.txt') as fp:
    tmp = fp.read().split('\n')
    init_state = list(tmp[0].split(' ')[-1])
    notes = [x.split(' => ') for x in tmp[1:] if x]

# Padd the state (guesstimation..)
left_pad_size = 20
right_pad_size = 200
left_pad = np.array(['.' for x in range(left_pad_size)])
right_pad = np.array(['.' for x in range(right_pad_size)])
state = left_pad + init_state + right_pad

gen = 50000000000
collaps_gen = 0

for i in range(1, 5000):
    new_state = np.array([x for x in state])
    for j in range(2, len(state)-1):
        current = ''.join(state[j-2:j+3])

        found = False
        for note in notes:
            if note[0] == current:
                new_state[j] = note[1]
                found = True
        if not found:
            new_state[j] = '.'

    if state[:-1] == new_state[1:]:
        collaps_gen = i
        state = new_state
        break

    state = new_state


nr = np.array[x+(gen-collaps_gen) for x in range(-left_pad_size, len(state))])
print(np.array([nr[k] for k, x in enumerate(state) if x == '#']).sum())
