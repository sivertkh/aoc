# --- Day 3: Crossed Wires ---
# Part 1 -

from pprint import pprint
with open('./input.txt') as fp:
    paths = [x.split(',') for x in fp.read().split('\n') if x]
    print(paths)


grid_size = 20000
grid = [['.' for x in range(grid_size)] for _ in range(grid_size)]

start_x = grid_size//2
start_y = grid_size//2

grid[start_x][start_y] = 'o'

crosses = []
for i, path in enumerate(paths):
    current_x = start_x
    current_y = start_y
    for step in path:
        direction = step[0]
        steps = int(step[1:])

        if direction == 'U':
            for _ in range(steps):
                current_x -= 1
                if grid[current_x][current_y] == '.' or grid[current_x][current_y] == f'{i}':
                    grid[current_x][current_y] = f'{i}'
                else:
                    grid[current_x][current_y] = 'X'
                    crosses.append([current_x, current_y])
        elif direction == 'D':
            for _ in range(steps):
                current_x += 1
                if grid[current_x][current_y] == '.' or grid[current_x][current_y] == f'{i}':
                    grid[current_x][current_y] = f'{i}'
                else:
                    grid[current_x][current_y] = 'X'
                    crosses.append([current_x, current_y])
        elif direction == 'R':
            for _ in range(steps):
                current_y += 1
                if grid[current_x][current_y] == '.' or grid[current_x][current_y] == f'{i}':
                    grid[current_x][current_y] = f'{i}'
                else:
                    grid[current_x][current_y] = 'X'
                    crosses.append([current_x, current_y])
        elif direction == 'L':
            for _ in range(steps):
                current_y -= 1
                if grid[current_x][current_y] == '.' or grid[current_x][current_y] == f'{i}':
                    grid[current_x][current_y] = f'{i}'
                else:
                    grid[current_x][current_y] = 'X'
                    crosses.append([current_x, current_y])

print(crosses)

min_dist = -1

for cross in crosses:
    dist = abs(start_x - cross[0]) + abs(start_y - cross[1])
    if min_dist == -1 or dist < min_dist:
        min_dist = dist

print(min_dist)
