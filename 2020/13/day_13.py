# --- Day 13: Shuttle Search ---
import itertools


with open('input.txt') as fp:
    depart_time = int(fp.readline().rstrip())
    buss_times = fp.read().rstrip().split(',')


buss_depart = [int(x) for x in buss_times if x != 'x']
depart = buss_depart.copy()
while True:
    possible_busses = [x for x in depart if x >= depart_time]
    if possible_busses:
        buss_id = depart.index(possible_busses[0])
        print(f'Part1: {buss_depart[buss_id] * (possible_busses[0] - depart_time)}')
        break
    depart = [depart[i] + v for i, v in enumerate(buss_depart)]


def find_step(start, step, shift, busses):
    start_shift = -1
    jmp = 0
    for i in itertools.count(start=start, step=step):
        if all([(i + shift[j]) % x == 0 for j, x in enumerate(busses)]):
            if start_shift == -1:
                start_shift = i
            else:
                jmp = i-start_shift
                break
    return start_shift, jmp


diffs = [buss_times.index(str(x)) for x in buss_depart]
start = 0
step = buss_depart[0]
for i in range(10):
    start, step = find_step(start, step, diffs, buss_depart[:i])
print(f'Part 2: {start}')
