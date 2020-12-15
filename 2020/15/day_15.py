# --- Day 15: Rambunctious Recitation ---

def solver(start, iterations):
    last = 0
    spoken = {}

    for i, s in enumerate(start):
        last = s
        spoken[s] = [i, i]

    for i in range(len(start), iterations):
        if spoken[last][0] == spoken[last][1]:
            if 0 in spoken:
                spoken[0][0] = spoken[0][1]
                spoken[0][1] = i
            else:
                spoken[0] = [i, i]
            last = 0
        else:
            nr = spoken[last]
            diff = nr[1] - nr[0]

            if diff in spoken:
                spoken[diff][0] = spoken[diff][1]
                spoken[diff][1] = i
            else:
                spoken[diff] = [i, i]
            last = diff
    return last


with open('input.txt') as fp:
    start_nr = [int(x) for x in fp.readline().rstrip().split(',')]

print(f'Part 1: {solver(start_nr, 2020)}')
print(f'Part 2: {solver(start_nr, 30000000)}')
