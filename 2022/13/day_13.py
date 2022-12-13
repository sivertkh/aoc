# --- Day 13: Distress Signal ---

import json
from functools import cmp_to_key

from aocd.models import Puzzle


def packet_cmp(left: str, right):
    if type(left) == int and type(right) == int:
        if left == right:
            return 0
        if left < right:
            return -1
        return 1

    if type(left) == int:
        return packet_cmp([left], right)
    if type(right) == int:
        return packet_cmp(left, [right])

    for x in range(len(left)):
        if x >= len(right):
            return 1
        order = packet_cmp(left[x], right[x])
        if order == -1:
            return -1
        if order == 1:
            return 1

    if len(right) > len(left):
        return -1

    return 0


def solve():
    puzzle = Puzzle(year=2022, day=13)

    part_1 = []
    part_2 = 0
    data = [
        [json.loads(y) for y in x.split("\n") if y]
        for x in puzzle.input_data.split("\n\n")
        if x
    ]

    for i, d in enumerate(data, 1):
        left, right = d
        if packet_cmp(left, right) == -1:
            part_1.append(i)

    part_1 = sum(part_1)

    # Flatten list for part 2
    data = [y for x in data for y in x]
    data.extend([[[2]], [[6]]])
    data.sort(key=cmp_to_key(packet_cmp))
    part_2 = (data.index([[2]]) + 1) * (data.index([[6]]) + 1)

    # puzzle.answer_a = part_1
    # puzzle.answer_b = part_2
    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 5292
assert part_2 == 23868
