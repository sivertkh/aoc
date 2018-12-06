#
# Part 1 -


def find_manhattan_distance(point_1, point_2):

    x = abs(point_1[0] - point_2[0])
    y = abs(point_1[1] - point_2[1])

    return x + y


with open('input.txt') as fp:
    coords = [[int(y) for y in x.rsplit('\n')[0].split(',')]
              for x in fp]


# (y, x)

max_y = max([x[0] for x in coords]) + 40
max_x = max([x[1] for x in coords]) + 40

print(f'({max_y}, {max_x})')

area = [['.' for x in range(max_x)] for y in range(max_y)]

names = [x for x in range(1, len(coords)+2)]
#names = ['A', 'B', 'C', 'D', 'E', 'F']

name_lookup = {}
for i, coord in enumerate(coords):
    area[coord[1]][coord[0]] = names[i]
    name_lookup[str(coord)] = names[i]


# For each element in area, find the closest coord in manhattan distance


# (y, x)

for x in range(len(area)):
    for y in range(len(area[0])):
        shortest = max_x * max_y
        name = '.'
        for coord in coords:
            distance = find_manhattan_distance((y, x), coord)

            if distance < shortest:
                shortest = distance
                name = name_lookup[str(coord)]
            elif distance == shortest:
                name = '.'

        area[x][y] = name

# Find and remove all on an edge

# 0,0 0,1 0,2 ...   0,max_x
# 1,0               1,max_x
# 2,0               2,max_x
# ...               ...
# max_y,0           max_x,max_y


# (y, x)

remove = set()
for x in range(len(area)):
    for y in range(len(area[0])):

        if x == 0 or y == 0 or x == max_x or y == max_y:
            remove.add(area[x][y])

remove.remove('.')
candidates = set(names) - remove

largest = 0
for candidate in candidates:
    a = sum([sum([1 for x in y if x == candidate]) for y in area])

    if a > largest:
        largest = a

print(largest)
