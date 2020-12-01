# --- Day 4: High-Entropy Passphrases ---
# Part 1 - OK

with open('input.txt', 'r') as fp:
    pws = [[s for s in line.rstrip().split(" ")] for line in fp]

print(sum([1 for x in pws if len(set(x)) == len(x)]))
