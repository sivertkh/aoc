# --- Day 3: Rucksack Reorganization ---

import numpy as np


def load_input():
    with open("input.txt") as fp:
        return [list(y.strip()) for y in fp.readlines()]


def get_item_priority(item):
    if item.isupper():
        return ord(item) - ord("A") + 27
    return ord(item) - ord("a") + 1


def solve(d):
    return (
        sum(
            [
                get_item_priority(
                    "".join(set(x[: len(x) // 2]).intersection(set(x[len(x) // 2 :])))
                )
                for x in d
            ]
        ),
        sum(
            [
                get_item_priority("".join(set.intersection(*[set(y) for y in x])))
                for x in np.array_split(np.array(d, dtype=object), len(d) // 3)
            ]
        ),
    )


part_1, part_2 = solve(load_input())
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
