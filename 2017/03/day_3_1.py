# --- Day 3: Spiral Memory ---
# Part 1 - ok
from math import sqrt, ceil

number = 325489
#number = 25

# We cheat by make it bigger then it needs to
size = int(ceil(sqrt(number))*2)
array = [[-1 for i in range(size)] for j in range(size)]

# Find a center
center = int(ceil(size/2))
array[center][center] = 1

i = 2
cur_x = center
cur_y = center
while i <= number:

    north_x = cur_x
    north_y = cur_y - 1
    north = array[north_y][north_x]

    south_x = cur_x
    south_y = cur_y + 1
    south = array[south_y][south_x]

    west_x = cur_x - 1
    west_y = cur_y
    west = array[west_y][west_x]

    east_x = cur_x + 1
    east_y = cur_y
    east = array[east_y][east_x]

    if north is -1 and west is -1 and south is -1 and east is -1:
        # Move easte
        cur_x = east_x
        cur_y = east_y
    elif north is -1 and west is not -1 and south is -1 and east is -1:
        # Move north
        cur_x = north_x
        cur_y = north_y
    elif north is -1 and west is -1 and south is not -1:
        # move west
        cur_x = west_x
        cur_y = west_y
    elif west is -1 and south is -1 and east is not -1:
        # move south
        cur_x = south_x
        cur_y = south_y
    elif north is not -1 and east is -1:
        # move east
        cur_x = east_x
        cur_y = east_y
    elif west is not -1 and north is -1:
        # moving north
        cur_x = north_x
        cur_y = north_y

    array[cur_y][cur_x] = i
    i = i + 1

# find the diff between center and cur_y and center and cur_x
y = abs(center-cur_y)
x = abs(center-cur_x)

print(x+y)
