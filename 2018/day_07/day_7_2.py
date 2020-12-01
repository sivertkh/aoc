# --- Day 7: The Sum of Its Parts ---
# Part 2 - ok

with open('input.txt') as fp:
    data = [x.split(' ') for x in fp.read().split('\n') if x]

requirments = {}
for i in data:
    if i[7] not in requirments:
        requirments[i[7]] = set()
    requirments[i[7]].add(i[1])

all_req = []
for k, v in requirments.items():
    all_req = all_req + list(v)

nr_workers = 5
step_base = 60
possible = list(set(all_req) - set(requirments.keys()))
path = []
workers = []

for i in range(nr_workers):
    workers.append({'id': i,
                    'job': '.',
                    'work_time': 0,
                    'comp_time': 0,
                    'free': True
                  })

sec = 0
comp_times = {chr(x): x-64+step_base for x in range (65, 91)}
while True:
    comp = []

    for x in [x for x in workers if not x['free']]:
        x['work_time'] += 1
        if x['work_time'] == x['comp_time']:
            path.append(x['job'])
            comp.append(x['job'])
            x['job'] = '.'
            x['work_time'] = 0
            x['comp_time'] = 0
            x['free'] = True

    new_req = {}
    for k, v in requirments.items():
        for c in comp:
            if c in v:
                v.remove(c)

        if len(v) != 0:
            new_req[k] = v
        else:
            possible.append(k)
    requirments = new_req

    possible.sort()
    free_workers = [x for x in workers if x['free']]
    for worker in free_workers:
        if len(possible) > 0:
            worker['free'] = False
            worker['job'] = possible[0]
            worker['comp_time'] = comp_times[possible[0]]
            possible = possible[1:]

    free_workers = [x for x in workers if x['free']]
    if len(free_workers) == nr_workers:
        # Done when no workers are assigned
        break

    sec += 1

print(''.join(path))
print(sec)
