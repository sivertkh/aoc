import itertools

# --- Day 1: Report Repair ---

with open('./input.txt') as fp:
    data = set([int(x.rstrip()) for x in fp.readlines()])

result = list(data.intersection(set([2020-x for x in data])))
print(f'Part 1: {result[0]*result[1]}')

# --- Part Two ---

for x in data:
    part_sum = 2020-x
    possible_values = list(set(range(part_sum+1)).intersection(data))
    result = [y for y in list(itertools.combinations(possible_values, 2))
              if y[0] + y[1] == part_sum]
    if result:
        print(f'Part 2: {x * result[0][0] * result[0][1]}')
        break
