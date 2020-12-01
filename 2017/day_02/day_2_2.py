# --- Day 2: Corruption Checksum ---
# Part 2 - ok

with open('./input.txt', 'r') as fp:
    data = [[int(x) for x in line.rstrip().split("\t")] for line in fp]

checksum = 0
for line in data:
    for number in line:
        a = [(number, y) for y in line if number != y and number % y == 0]

        if len(a) > 0:
            checksum += a[0][0] // a[0][1]
            break
print(checksum)
