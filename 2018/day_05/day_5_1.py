# --- Day 5: Alchemical Reduction ---
# Part 1 - ok

with open('input.txt') as fp:
    polymer = list(fp.read().rstrip('\n'))

while True:
    copy = []
    skip = False
    for i in range(len(polymer)-1):
        if skip:
            skip = False
            continue

        diff = abs(ord(polymer[i]) - ord(polymer[i+1]))
        if diff == 32:
            skip = True
            continue
        copy.append(polymer[i])

    if not skip:
        copy.append(polymer[-1])

    if len(copy) < len(polymer):
        polymer = copy
    else:
        print('No diff!')
        break

print(len(polymer))
