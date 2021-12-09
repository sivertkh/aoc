# --- Day 5: Hydrothermal Venture ---

with open("input.txt") as fp:
    lines = [x.strip().split(' -> ') for x in fp.readlines()]
    lines = [[y.split(',') for y in x] for x in lines]
    lines = [[list(map(int, y)) for y in x] for x in lines]

max_x = max([y[0] for x in lines for y in x])
max_y = max([y[1] for x in lines for y in x])

m_1 = [[0 for _ in range(max_y+1)] for _ in range(max_x+1) ]
m_2 = [[0 for _ in range(max_y+1)] for _ in range(max_x+1) ]

for line in lines:
    start_x, start_y = line[0]
    end_x, end_y = line[1]

    if start_x == end_x:
        if start_y > end_y:
            r = range(end_y, start_y+1)
        else:
            r = range(start_y, end_y+1)
        for y in r:
            m_1[y][start_x] += 1
            m_2[y][start_x] += 1
    elif start_y == end_y:
        if start_x > end_x:
            r = range(end_x, start_x+1)
        else:
            r = range(start_x, end_x+1)
        for x in r:
            m_1[start_y][x] += 1
            m_2[start_y][x] += 1
    else:
        if start_x > end_x:
            r_x = list(range(start_x, end_x-1, -1))
        else:
            r_x = list(range(start_x, end_x+1))

        if start_y > end_y:
            r_y = list(range(start_y, end_y-1, -1))
        else:
            r_y = list(range(start_y, end_y+1))

        for i, y in enumerate(r_y):
            m_2[y][r_x[i]] += 1


print(f"Part 1: {sum([1 for x in m_1 for y in x if y > 1])}")
print(f"Part 2: {sum([1 for x in m_2 for y in x if y > 1])}")
