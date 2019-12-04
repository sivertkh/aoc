# --- Day 4: Secure Container ---
# Part 1 - ok

with open('./input.txt') as fp:
    pw_range = [int(x) for x in fp.read().split('-') if x]

matches = 0

for nr in range(pw_range[0], pw_range[1]):
    nr_split = [int(i) for i in str(nr)]
    # Two adjacent digits
    if min([len(set(x)) for x in zip(nr_split[:-1], nr_split[1:])]) != 1:
        continue
    # Never decreasing
    nr_sorted = nr_split[:]
    nr_sorted.sort()
    if nr_split != nr_sorted:
        continue
    matches += 1

print(matches)
