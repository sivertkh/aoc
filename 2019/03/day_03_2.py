# --- Day 3: Crossed Wires ---
# Part 2 -

from pprint import pprint
with open('./input.txt') as fp:
    paths = [x.split(',') for x in fp.read().split('\n') if x]
    print(paths)


grid_size = 20000
grid = [['.' for x in range(grid_size)] for _ in range(grid_size)]

print('Grid created')

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
                if grid[current_x][current_y] == '.':
                    grid[current_x][current_y] = f'{i}'
                elif grid[current_x][current_y] == f'{i}':
                    # Corssing outself..
                    grid[current_x][current_y] = 'S'
                else:
                    grid[current_x][current_y] = 'X'
                    crosses.append([current_x, current_y])
        elif direction == 'D':
            for _ in range(steps):
                current_x += 1
                if grid[current_x][current_y] == '.':
                    grid[current_x][current_y] = f'{i}'
                elif grid[current_x][current_y] == f'{i}':
                    grid[current_x][current_y] = 'S'
                else:
                    grid[current_x][current_y] = 'X'
                    crosses.append([current_x, current_y])
        elif direction == 'R':
            for _ in range(steps):
                current_y += 1
                if grid[current_x][current_y] == '.':
                    grid[current_x][current_y] = f'{i}'
                elif grid[current_x][current_y] == f'{i}':
                    grid[current_x][current_y] = 'S'
                else:
                    grid[current_x][current_y] = 'X'
                    crosses.append([current_x, current_y])
        elif direction == 'L':
            for _ in range(steps):
                current_y -= 1
                if grid[current_x][current_y] == '.':
                    grid[current_x][current_y] = f'{i}'
                elif grid[current_x][current_y] == f'{i}':
                    grid[current_x][current_y] = 'S'
                else:
                    grid[current_x][current_y] = 'X'
                    crosses.append([current_x, current_y])

path_lengths = []

for cross in crosses:
    combind_path = 0
    print(f'Working on corss {cross}')
    for path in ['0', '1']:
        path_length = 0
        last_move = 'o'
        cur_x = start_x
        cur_y = start_y

        while True:
            if cur_x == cross[0] and cur_y == cross[1]:
                combind_path += path_length
                break
            # U

            if grid[cur_x][cur_y] == 'S':
                # If we cross ourself, we continue in the current direction
                if last_move == 'U':
                    cur_x -= 1
                elif last_move == 'D':
                    cur_x += 1
                elif last_move == 'R':
                    cur_y += 1
                elif last_move == 'L':
                    cur_y -= 1
                path_length += 1

            elif grid[cur_x-1][cur_y] in [path, 'X', 'S'] and last_move != 'D':
                cur_x -= 1
                path_length += 1
                last_move = 'U'
            # D
            elif grid[cur_x+1][cur_y] in [path, 'X', 'S'] and last_move != 'U':
                cur_x += 1
                path_length += 1
                last_move = 'D'
            # R
            elif grid[cur_x][cur_y+1] in [path, 'X', 'S'] and last_move != 'L':
                cur_y += 1
                path_length += 1
                last_move = 'R'
            # L
            elif grid[cur_x][cur_y-1] in [path, 'X', 'S'] and last_move != 'R':
                cur_y -= 1
                path_length += 1
                last_move = 'L'
            else:
                break

            #tmp = grid[cur_x][cur_y]
            #grid[cur_x][cur_y] = '*'
            # for x in grid[cur_x-10:cur_x+10]:
            #    print(x[cur_y-10:cur_y+10])
            #print(f'At x: {cur_x}, y: {cur_y}')
            # input('continue')
            #grid[cur_x][cur_y] = tmp

    path_lengths.append(combind_path)

print(path_lengths)
print(min(path_lengths))
