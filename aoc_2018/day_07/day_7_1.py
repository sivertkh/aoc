# --- Day 7: The Sum of Its Parts ---
# Part 1 - ok


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

possible = list(set(all_req) - set(requirments.keys()))
path = []
while len(possible) > 0:
    possible.sort()
    comp = possible[0]
    path.append(comp)
    possible = possible[1:]

    # Remove completed from requriments lists and
    # recalculate

    new_req = {}
    for k, v in requirments.items():
        print(v)
        if comp in v:
            v.remove(comp)
        if len(v) != 0:
            new_req[k] = v
        else:
            possible.append(k)
    requirments = new_req

print(''.join(path))
