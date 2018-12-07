# --- Day 7: The Sum of Its Parts ---
# Part 2 -


with open('input.txt') as fp:
    data = [x.split(' ') for x in fp.read().split('\n') if x]

requirments = {}
for i in data:
    if i[7] not in requirments:
        requirments[i[7]] = set()

    requirments[i[7]].add(i[1])

# Find starts
all_req = []
for k, v in requirments.items():
    all_req = all_req + list(v)


nr_workers = 5
step_base = 60

possible = list(set(all_req) - set(requirments.keys()))
path = []

workers = []

for i in range(nr_workers):
    workers[i] = {'nr': i,
                  'job': None,
                  'work_time': 0,
                  'comp_time': 0,
                  'free': True,
                  }


sec = 0
total_time = 0
while len(requirments) > 0:

    # Update work time
    comp = []

    for x in [x for x in workers if not x['free']]:
        x['work_time'] += 1

        if x['work_time'] == x['comp_time']:
            total_time += x['work_time']
            path.append(x['job'])
            comp.append(x['job'])
            x['job'] = None
            x['work_time'] = 0
            x['comp_time'] = 0
            x['free'] = True

    # Remove completed from requriments lists and
    # recalculate

    new_req = {}
    for k, v in requirments.items():
        print(v)
        for c in comp:
            if c in v:
                v.remove(c)

        if len(v) != 0:
            new_req[k] = v
        else:
            possible.append(k)
    requirments = new_req

    # recalculate and assign to free workers
    possible.sort()

    free_workers = [x for x in workers if x['free']]

    for worker in free_workers:

        if len(possible) == 0:
            break

        worker['free'] = False
        worker['job'] = possible[0]
        worker['comp_time'] = 0

        possible = possible[1:]

    sec += 1

print(''.join(path))
