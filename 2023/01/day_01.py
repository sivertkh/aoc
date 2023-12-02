# AOC 2023
# --- Day 1: Trebuchet?! ---
from typing import List


def solve_part_1(lines: List[str]) -> int:
    res = 0
    for x in lines:
        a = [s for s in x if s.isdigit()]
        res += int(f"{a[0]}{a[-1]}")
    return res


def solve_part_2(lines: List[str]) -> int:
    numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]
    res = 0
    for l in lines:
        a = [l.rfind(x) for x in numbers]
        max_ix = a.index(max(a))
        last_nr = str(int(max_ix) - 8) if max_ix > 8 else max_ix + 1

        a = [1000 if x == -1 else x for x in [l.find(x) for x in numbers]]
        min_ix = a.index(min(a))
        first_nr = str(int(min_ix) - 8) if min_ix > 8 else min_ix + 1

        res += int(f"{first_nr}{last_nr}")

    return res


def solve():
    with open("input.txt") as fp:
        data = [x for x in fp.readlines() if x]

    return solve_part_1(data), solve_part_2(data)


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 55029
assert part_2 == 55686
