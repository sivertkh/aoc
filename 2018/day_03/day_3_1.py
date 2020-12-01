# --- Day 3: No Matter How You Slice It ---
# Part 1 - ok

with open('input.txt') as fp:
    claims = [x.rstrip().split(' ') for x in fp.readlines()]

# Approximate a max size ..
m = 1000
area = [['.' for x in range(0, m)] for y in range(0, m)]

for claim in claims:
    print(claim)
    claim_id = claim[0]
    pos_y, pos_x = claim[2].rstrip(':').split(',')
    size_y, size_x = claim[3].split('x')

    for x in range(int(pos_x), int(pos_x) + int(size_x)):
        for y in range(int(pos_y), int(pos_y) + int(size_y)):
            if area[x][y] is not '.':
                area[x][y] = 'X'
            else:
                area[x][y] = '#'

res = 0
for a in area:
    for l in a:
        if l is 'X':
            res += 1

print(res)
