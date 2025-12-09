"""
AOC 2025
--- Day 9: Movie Theater ---
"""

import itertools
from shapely.geometry import Polygon, box


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        data = [
            tuple(map(int, x.strip().split(","))) for x in fp.read().split("\n") if x
        ]

    point_area = []
    for a, b in itertools.combinations(data, 2):
        area = (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)
        point_area.append((a, b, int(area)))

    point_area.sort(key=lambda x: x[2], reverse=True)

    part_1_res = point_area[0][2]
    part_2_res = 0

    loop = Polygon(data)

    for a, b, area in point_area:
        if loop.contains(
            box(min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1]))
        ):
            part_2_res = area
            break

    return part_1_res, part_2_res


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

    assert part_1 == 4715966250
    assert part_2 == 1530527040
