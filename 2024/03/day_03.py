# AOC 2023
# --- Day 3: Mull It Over ---


import collections as coll
import re


def solve_part_1(data):

    return sum([int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", data)])


def solve_part_2(data):
    donts = coll.deque([m.end() for m in re.finditer(r"don't\(\)", data)])
    dos = coll.deque([m.end() for m in re.finditer(r"do\(\)", data)])

    res = 0
    start = 0
    end = donts.popleft()
    while True:
        res += sum(
            [
                int(a) * int(b)
                for a, b in re.findall(r"mul\((\d+),(\d+)\)", data[start:end])
            ]
        )

        while dos:
            tmp = dos.popleft()
            if tmp > end:
                start = tmp
                break
        else:
            break

        while donts:
            tmp = donts.popleft()
            if tmp > start:
                end = tmp
                break
        else:
            end = len(data)

    return res


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        data = fp.read().strip()
    return solve_part_1(data), solve_part_2(data)


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 191183308
assert part_2 == 92082041
