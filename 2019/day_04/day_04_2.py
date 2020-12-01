# --- Day 4: Secure Container ---
# Part 2 - ok

with open('./input.txt') as fp:
    pw_range = [int(x) for x in fp.read().split('-') if x]

matches = 0

#pw_range = [112233, 112234]

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

    duplates = []
    current_series = None
    last_nr = []
    for n in nr_split:
        if len(last_nr) == 0:
            last_nr.append(n)

        elif n == last_nr[0]:
            last_nr.append(n)
        else:
            duplates.append(last_nr)
            last_nr = [n]

    if len(last_nr) >= 2:
        duplates.append(last_nr)

    if not 2 in [len(x) for x in duplates]:
        continue

    matches += 1

print(matches)
