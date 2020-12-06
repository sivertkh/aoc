# --- Day 6: Custom Customs ---

with open('./input.txt') as fp:
    ans = [[list(y) for y in x.rstrip().split('\n')] for x in fp.read().split('\n\n')]

print(f'Part 1: {sum([len(set(x)) for x in [[y for x in z for y in x] for z in ans]])}')
print(f'Part 2: {sum([len(set.intersection(*[set(y) for y in x])) for x in ans])}')
