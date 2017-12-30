# --- Day 22: Sporifica Virus ---
# part 1 - ok

import numpy as np

with open('input.txt', 'r') as fp:
    start_state = np.array([[y for y in x.rstrip()] for x in fp], dtype=str)

bursts = 10000
new_size = bursts // 5
center = (new_size // 2) - (len(start_state) // 2)

inf_array = np.empty((new_size, new_size), dtype=str)
inf_array[:] = '.'
inf_array[center:center+len(start_state),center:center+len(start_state)] = start_state

start_pos = center + (len(start_state) // 2)
y_pos = start_pos
x_pos = start_pos
direction = 'n'
infected = 0
# left = counterclockwise, right = clockwise
for i in range(0,bursts):
    if inf_array[y_pos][x_pos] == '.':
        # Clean
        # Turn left
        if direction == 'n':
            # n -> w
            direction = 'w'
        elif direction == 'w':
            # w -> s
            direction = 's'
        elif direction == 's':
            # s -> e
            direction = 'e'
        elif direction == 'e':
            # e -> n
            direction = 'n'
        inf_array[y_pos][x_pos] = '#'
        infected = infected + 1
    elif inf_array[y_pos][x_pos] == '#':
        # Infected!
        # Turn right
        if direction == 'n':
            # n -> e
            direction = 'e'
        elif direction == 'w':
            # w -> n
            direction = 'n'
        elif direction == 's':
            # s -> w
            direction = 'w'
        elif direction == 'e':
            # e -> s
            direction = 's'
        inf_array[y_pos][x_pos] = '.'
    else:
        print("ERROR!!")
        exit(1)

    # Move to the next node
    if direction == 'n':
        y_pos = y_pos - 1
    elif direction == 'w':
        x_pos = x_pos - 1
    elif direction == 's':
        y_pos = y_pos + 1
    elif direction == 'e':
        x_pos = x_pos + 1
    else:
        print("Error, unknown direction..")
        exit(1)

print(infected)
