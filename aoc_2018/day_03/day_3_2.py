# --- Day 3: No Matter How You Slice It ---
# Part 2 - ok

with open('input.txt') as fp:
    claims = [x.rstrip().split(' ') for x in fp.readlines()]

# Approximate a max size ..
m = 2000
area = [['.' for x in range(0, m)] for y in range(0, m)]

claim_area = {}

for claim in claims:
    claim_id = claim[0]
    pos_y, pos_x = claim[2].rstrip(':').split(',')
    size_y, size_x = claim[3].split('x')

    claim_area[claim_id] = int(size_y) * int(size_x)
    for x in range(int(pos_x), int(pos_x) + int(size_x)):
        for y in range(int(pos_y), int(pos_y) + int(size_y)):
            if area[x][y] is not '.':
                area[x][y] = 'X'
            else:
                area[x][y] = claim_id

new_area = {}
for a in area:
    for l in a:
        if l is not 'X' and l is not '.':
            if l in new_area:
                new_area[l] += 1
            else:
                new_area[l] = 1

for k, v in new_area.items():
    if claim_area[k] == v:
        print(f'Found area! {k}')
        break
