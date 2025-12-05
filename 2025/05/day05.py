"""
AOC 2025
--- Day 5: Cafeteria ---
"""

import numpy as np


def merge_ranges(ranges: np.ndarray) -> np.ndarray:
    """Merges overlapping ranges."""

    ranges = ranges[ranges[:, 0].argsort()]

    merged_ranges = []
    if len(ranges) > 0:
        merged_ranges.append(list(ranges[0]))

        for i in range(1, len(ranges)):
            start, end = ranges[i]
            _, merged_end = merged_ranges[-1]

            if start <= merged_end:
                merged_ranges[-1][1] = max(merged_end, end)
            else:
                merged_ranges.append([start, end])
    return np.array(merged_ranges)


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        ranges, ingridients = fp.read().split("\n\n", maxsplit=1)

    ranges = np.array([list(map(int, x.split("-"))) for x in ranges.split("\n") if x])
    ingridients = [int(x.strip()) for x in ingridients.split("\n") if x]

    part_1_res = sum(
        1 for i in ingridients if np.any((i >= ranges[:, 0]) & (i <= ranges[:, 1]))
    )
    part_2_res = sum(stop - start + 1 for start, stop in merge_ranges(ranges))

    return part_1_res, part_2_res


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

    assert part_1 == 775
    assert part_2 == 350684792662845
