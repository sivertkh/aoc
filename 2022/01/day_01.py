# --- Day 1: Calorie Counting ---


def load_input():
    with open("input.txt") as fp:
        x = fp.read()
        x = [y.split("\n") for y in x.split("\n\n")]
    return x


def solve(d):
    s = [sum([int(y) for y in x if y]) for x in d]
    s.sort()
    return s[-1], sum(s[-3:])


part_1, part_2 = solve(load_input())
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
