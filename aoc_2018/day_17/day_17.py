# --- Day 17: Reservoir Research ---
# Part 1 and 2- ok

from collections import deque

with open('input.txt') as fp:
    # with open('input.txt') as fp:
    data = [x.split(', ') for x in fp.read().split('\n') if x]

inputs = []
for d in data:
    a = {}
    tmp = d[0].split('=')
    a[tmp[0]] = [int(tmp[1])]

    tmp_2 = d[1].split('=')
    second_1, second_2 = tmp_2[1].split('..')

    a[tmp_2[0]] = [int(second_1), int(second_2)]
    inputs.append(a)

# find min/max x and min/max y
xs = [x['x'] for x in inputs]
min_x = min([item for sublist in xs for item in sublist]) - 1
max_x = max([item for sublist in xs for item in sublist]) + 2

ys = [x['y'] for x in inputs]
min_y = min([item for sublist in ys for item in sublist])
max_y = max([item for sublist in ys for item in sublist]) + 1

area = [['.' for x in range(min_x, max_x+1)] for y in range(0, max_y)]

# Set spring
area[0][500-min_x] = '+'

# Fill in clay
for i in inputs:
    if len(i['x']) > 1:
        xs = range(i['x'][0], i['x'][1]+1)
    else:
        xs = range(i['x'][0], i['x'][0]+1)

    if len(i['y']) > 1:
        ys = range(i['y'][0], i['y'][1]+1)
    else:
        ys = range(i['y'][0], i['y'][0]+1)

    for x in xs:
        for y in ys:
            area[y][x-min_x] = '#'

q = deque()
q.append([0, 500-min_x])

while len(q) > 0:
    cur = q.popleft()
    fall_y = cur[0]
    fall_x = cur[1]

    while fall_y < max_y-1:
        if area[fall_y+1][fall_x] == '.':
            area[fall_y+1][fall_x] = '|'
            fall_y += 1

        elif area[fall_y+1][fall_x] == '#' or area[fall_y+1][fall_x] == '~':
            found_left = False
            left_overflow = False
            left_end = fall_x

            found_right = False
            right_overflow = False
            right_end = fall_x

            while not found_left:
                if area[fall_y+1][left_end] != '#' and area[fall_y+1][left_end] != '~':
                    found_left = True
                    left_overflow = True
                else:
                    if area[fall_y][left_end] == '#':
                        found_left = True
                        left_end += 1
                    else:
                        left_end -= 1

            while not found_right:
                if area[fall_y+1][right_end] != '#' and area[fall_y+1][right_end] != '~':
                    found_right = True
                    right_overflow = True
                else:
                    if area[fall_y][right_end] == '#':
                        found_right = True
                        right_end -= 1
                    else:
                        right_end += 1

            if left_overflow and right_overflow:
                for x in range(left_end, right_end+1):
                    area[fall_y][x] = '|'
                fall_x = right_end
                q.append([fall_y, left_end])
            elif left_overflow:
                if [fall_y, left_end] in q:
                    q.remove([fall_y, left_end])
                for x in range(left_end, right_end+1):
                    area[fall_y][x] = '|'
                fall_x = left_end
            elif right_overflow:
                if [fall_y, right_end] in q:
                    q.remove([fall_y, right_end])
                for x in range(left_end, right_end+1):
                    area[fall_y][x] = '|'
                fall_x = right_end

            else:
                for x in range(left_end, right_end+1):
                    area[fall_y][x] = '~'
                fall_y -= 1
        elif area[fall_y+1][fall_x] == '|':
            # Moving down into existing pool. Skipping
            break

water_area = 0
at_rest = 0
for d in area[min_y:max_y]:
    water_area += sum([1 for x in d if x == '|' or x == '~'])
    at_rest += sum([1 for x in d if x == '~'])

print(f'part1: {water_area}')
print(f'part2: {at_rest}')
