# AOC 2024
# --- Day 5: Print Queue ---

import functools


def compare(order, a: int, b: int) -> int:
    if a == b:
        return 0
    if b in [k[1] for k in order if k[0] == a]:
        return -1

    return 1


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        order, updates = [x for x in fp.read().split("\n\n") if x]
        order = [
            list(map(int, [y for y in x.split("|") if y]))
            for x in order.split("\n")
            if x
        ]
        updates = [
            list(map(int, [y for y in x.split(",") if y]))
            for x in updates.split("\n")
            if x
        ]
    p1, p2 = 0, 0
    for update in updates:
        s = sorted(update, key=functools.cmp_to_key(lambda a, b: compare(order, a, b)))
        if update == s:
            p1 += update[len(update) // 2]
        else:
            p2 += s[len(s) // 2]

    return p1, p2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 4790
assert part_2 == 6319
