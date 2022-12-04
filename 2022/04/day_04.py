# --- Day 4: Camp Cleanup ---


def load_input():
    with open("input.txt") as fp:
        return [
            list(map(lambda x: list(map(int, x.split("-"))), x.strip().split(",")))
            for x in fp.readlines()
        ]


def solve(d):
    part_1 = part_2 = 0

    for a, b in d:
        if a[0] >= b[0] and a[1] <= b[1] or b[0] >= a[0] and b[1] <= a[1]:
            part_1 += 1
        if len(set(range(a[0], a[1] + 1)).intersection(range(b[0], b[1] + 1))) != 0:
            part_2 += 1

    return part_1, part_2


part_1, part_2 = solve(load_input())
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
