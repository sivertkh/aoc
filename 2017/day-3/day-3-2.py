# --- Day 3: Spiral Memory ---
# part 2 - OK
from math import sqrt, ceil

# * Generate array
# * Find path
# * profit


number = 265149
#number = 807

# We need to create a array with space for the spiral.
# Use the "simple" solution where we set the size as the square root of the
# input. We round this number up.

# We "cheat" by make it bigger then it needs to.. Finding the position then
# becomes simple..
size = int(ceil(sqrt(number))/2)

# Initiate the array
array = [[-1 for i in range(size)] for j in range(size)]

# Find a center
center = int(ceil(size/2))

array[center][center] = 1

cur_x = center
cur_y = center


value = 1
while value <= number:

    north_x = cur_x
    north_y = cur_y - 1
    north = array[north_y][north_x]

    south_x = cur_x
    south_y = cur_y + 1
    south = array[south_y][south_x]

    west_x = cur_x -1
    west_y = cur_y
    west = array[west_y][west_x]

    east_x = cur_x + 1
    east_y = cur_y
    east = array[east_y][east_x]

    # if S is -1, North is -1, E is not -1

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
    else:
        print("No where to move!! ERROR!")
        exit(1)

    # find the adjacent values

    # Recalculating after moving..
    north_x = cur_x
    north_y = cur_y - 1
    north = array[north_y][north_x]

    south_x = cur_x
    south_y = cur_y + 1
    south = array[south_y][south_x]

    west_x = cur_x -1
    west_y = cur_y
    west = array[west_y][west_x]

    east_x = cur_x + 1
    east_y = cur_y
    east = array[east_y][east_x]

    # Calculate the diagonal values
    # NW
    nw_x = cur_x - 1
    nw_y = cur_y - 1
    nw = array[nw_y][nw_x]

    # NE
    ne_x = cur_x + 1
    ne_y = cur_y - 1
    ne = array[ne_y][ne_x]

    # SW
    sw_x = cur_x - 1
    sw_y = cur_y + 1
    sw = array[sw_y][sw_x]

    # SE
    se_x = cur_x + 1
    se_y = cur_y + 1
    se = array[se_y][se_x]

    s = 0
    if north != -1:
        s = s + north
    if west != -1:
        s = s + west
    if south != -1:
        s = s + south
    if east != -1:
        s = s + east

    if nw != -1:
        s = s + nw
    if ne != -1:
        s = s + ne
    if sw != -1:
        s = s + sw
    if se != -1:
        s = s + se

    array[cur_y][cur_x] = s
    value = s

print(value)
