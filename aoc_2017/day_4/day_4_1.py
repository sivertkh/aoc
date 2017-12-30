# --- Day 4: High-Entropy Passphrases ---
# part 1 - OK

with open('input.txt', 'r') as fp:
    pp = [[s for s in line.rstrip().split(" ")] for line in fp]

valid = 0
for x in pp:
    s = set(x)

    if len(s) == len(x):
        valid = valid + 1

print(valid)
