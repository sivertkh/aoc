# --- Day 25: Four-Dimensional Adventure ---
# Part 1 - ok
# Part 2 -

from collections import deque


def manhattan_4d(a, b):
    return (abs(a[0]-b[0]) + abs(a[1]-b[1]) +
            abs(a[2]-b[2]) + abs(a[3]-b[3]))


def main():
    with open('input.txt') as fp:

        stars = [[int(y) for y in x.split(',')]
                 for x in fp.read().split('\n') if x]

    in_range = {}
    for star in stars:
        tmp = []
        for pos in stars:
            dist = manhattan_4d(star, pos)
            if dist <= 3:
                tmp.append(pos)
        in_range[','.join([str(x) for x in star])] = tmp

    visited = []
    constilations = 0

    for k, v in in_range.items():
        if k in visited:
            continue

        constilations += 1
        visited.append(k)

        cons = deque()
        cons.extend(v)
        while len(cons) > 0:
            cur = cons.popleft()
            cur_name = ','.join([str(x) for x in cur])

            if cur_name in visited:
                continue

            visited.append(cur_name)
            cons.extend([x for x in in_range[cur_name] if x not in visited])

    print(constilations)


if __name__ == "__main__":
    main()
