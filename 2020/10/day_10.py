# --- Day 10: Adapter Array ---
from collections import Counter


with open('input.txt') as fp:
    adapters = [int(x.rstrip()) for x in fp.readlines()]

adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()

differences = Counter([abs(j - i) for i, j in zip(adapters, adapters[1:])])
print(f'Part 1: {differences[1] * differences[3]}')


def memoize(f):
    m = {}

    def memoize(x):
        if x not in m:
            m[x] = f(x)
        return m[x]
    return memoize


@memoize
def find_path(pos):
    if pos == len(adapters) - 1:
        return 1

    children = []
    for i in range(pos+1, pos+4):
        if i < len(adapters) and abs(adapters[pos] - adapters[i]) <= 3:
            children.append(find_path(i))
    return(sum(children))


print(f'Part 2: {find_path(0)}')
