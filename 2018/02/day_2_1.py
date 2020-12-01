# --- Day 2: Inventory Management System ---
# Part 1 - ok

with open('./input.txt') as fp:
    pkg_ids = [x for x in fp.read().split('\n') if x]

twos = 0
threes = 0

for pkg_id in pkg_ids:
    count = {}
    for c in list(pkg_id):
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1

    if 2 in count.values():
        twos += 1
    if 3 in count.values():
        threes += 1

print(twos*threes)
