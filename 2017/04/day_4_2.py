# --- Day 4: High-Entropy Passphrases ---
# Part 2 - ok

with open('input.txt', 'r') as fp:
    pws = [[''.join(sorted(s)) for s in line.rstrip().split(" ")]
           for line in fp]

print(sum([1 for x in pws if len(set(x)) == len(x)]))
