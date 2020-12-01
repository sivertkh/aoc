# --- Day 11: Chronal Charge ---
# Part 1 - ok

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
for y in range(size-3):
    for x in range(size-3):
        s = cells[y:y+3, x:x+3].sum()
        if s > max_sum:
            max_sum = s
            x_pos = x
            y_pos = y

print(max_sum)
print(f'{x_pos+1},{y_pos+1}')
