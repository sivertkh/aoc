# --- Day 6: Chronal Coordinates ---
# Part 2 - ok


def find_manhattan_distance(point_1, point_2):
    x = abs(point_1[0] - point_2[0])
    y = abs(point_1[1] - point_2[1])
    return x + y


with open('input.txt') as fp:
    coords = [[int(y) for y in x.rsplit('\n')[0].split(',')]
              for x in fp]


max_y = max([x[0] for x in coords]) + 40
max_x = max([x[1] for x in coords]) + 40

area = [[0 for x in range(max_x)] for y in range(max_y)]
max_total_length = 10000

for x in range(len(area)):
    for y in range(len(area[0])):
        shortest = max_x * max_y

        total_length = sum([find_manhattan_distance((y, x), coord)
                            for coord in coords])

        if total_length < max_total_length:
            area[x][y] = 1

print(sum([sum([x for x in y]) for y in area]))
