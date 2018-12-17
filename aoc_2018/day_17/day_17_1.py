# --- Day 17: Reservoir Research ---
# Part 1 -

with open('simple.txt') as fp:
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

for i in inputs:
    print(i)

# find max x and max y

xs = [x['x'] for x in inputs]
min_x = min([item for sublist in xs for item in sublist]) - 1
max_x = max([item for sublist in xs for item in sublist]) + 1

ys = [x['y'] for x in inputs]
min_y = 0
max_y = max([item for sublist in ys for item in sublist]) + 1

area = [['.' for y in range(min_y, max_y)] for x in range(min_x, max_x)]

for d in area:
    print(''.join(d))

# Set spring
area[0][500-min_x] = '+'
print('\n--------------')
for d in area:
    print(''.join(d))
print('--------------\n')
for i in inputs:
    for x in i['x']:
        for y in i['y']:
            print(f'x:{x}, y:{y}')
            print(f'x:{x-min_x}, y:{y}')
            # area[y][x-min_x] = '#'

print('\n--------------')
for d in area:
    print(''.join(d))
print('--------------\n')
