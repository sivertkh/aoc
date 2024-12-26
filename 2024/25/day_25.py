# AOC 2024
# --- Day 25: Code Chronicle ---s

import numpy as np


def solve_part_1(keys: list, locks: list) -> int:
    return sum([sum([1 if np.all(l + k <= 5) else 0 for k in keys]) for l in locks])


def solve() -> int:
    with open("input.txt", encoding="utf-8") as fp:
        data = [
            np.array([list(y) for y in x.split("\n") if y])
            for x in fp.read().split("\n\n")
            if x
        ]

    keys, locks = [], []
    for x in data:
        if all((y == "#" for y in x[0])):
            locks.append(np.argmax(x, axis=0) - 1)
        else:
            keys.append(np.argmax(np.flipud(x), axis=0) - 1)

    return solve_part_1(keys, locks)


if __name__ == "__main__":
    part_1 = solve()
    print(f"Part 1: {part_1}")
    assert part_1 == 2885
