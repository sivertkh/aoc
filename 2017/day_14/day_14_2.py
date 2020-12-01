# --- Day 14: Disk Defragmentation ---
# part 2 - OK

from aoc_2017.day_10.day_10_2 import create_hash


def mark_neighbours(pos_i, pos_j, grid, nr):

    if pos_i < 0 or pos_i >= len(grid):
        return
    if pos_j < 0 or pos_j >= len(grid):
        return

    cur = grid[pos_i][pos_j]
    if cur >= 0:
        # Already visited or empty
        return

    grid[pos_i][pos_j] = nr

    mark_neighbours(pos_i-1, pos_j, grid, nr)
    mark_neighbours(pos_i+1, pos_j, grid, nr)
    mark_neighbours(pos_i, pos_j+1, grid, nr)
    mark_neighbours(pos_i, pos_j-1, grid, nr)


data = 'vbqugkhl'
grid = []
for i in range(128):
    tmp = [x for x in create_hash("{}-{}".format(data, i))]
    tmp2 = [bin(int(x, 16))[2:].rjust(4, "0") for x in tmp]
    grid.append([-1 if item == '1' else 0 for sublist in tmp2 for item in
                 sublist])

group_nr = 1
for i in range(len(grid)):
    for j in range(len(grid)):
        pos = grid[i][j]
        if pos == -1:
            # Not visited
            mark_neighbours(i, j, grid, group_nr)
            group_nr += 1


print(group_nr-1)
