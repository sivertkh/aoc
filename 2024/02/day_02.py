# AOC 2024
# --- Day 2: Red-Nosed Reports ---

import numpy as np


def is_sorted(a: list[int]) -> bool:
    """Test if array is sorted in ascending or descending order."""
    return a == sorted(a) or a == sorted(a, reverse=True)


def is_safe(r: list[int]) -> bool:
    """Check if a report is safe."""
    d = np.abs(np.diff(r))
    return np.all((d <= 3) & (d > 0)) and is_sorted(r)


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        data = [list(map(int, x.split())) for x in fp.read().split("\n") if x]
    p1 = p2 = 0
    for x in data:
        if is_safe(x):
            p1 += 1
        else:
            for i in range(len(x)):
                if is_safe(x[:i] + x[i + 1 :]):
                    p2 += 1
                    break
    return p1, p1 + p2


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
    assert part_1 == 598
    assert part_2 == 634
