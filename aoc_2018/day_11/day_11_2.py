# --- Day 11: Chronal Charge ---
# Part 2 - ok

import numpy as np

serial = 1308
size = 300

cells = np.array([np.array([0 for x in range(size)]) for y in range(size)])

for y in range(size):
    for x in range(size):

        rack_id = (x+1) + 10
        power_level = rack_id * (y+1)
        power_level += serial
        power_level = power_level * rack_id
        try:
            hundreds = int(str(power_level)[-3])
            cells[y][x] = hundreds - 5
        except IndexError as e:
            cells[y][x] = -5

max_sum = 0
x_pos = 0
y_pos = 0
max_size = 0

for i in range(1, size):
    for y in range(size-i):
        for x in range(size-i):
            s = cells[y:y+i, x:x+i].sum()
            if s > max_sum:
                max_sum = s
                x_pos = x
                y_pos = y
                max_size = i

print(max_sum)
print(f'{x_pos+1},{y_pos+1},{max_size}')
