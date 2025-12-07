"""
AOC 2025
--- Day 7: Laboratories ---
"""

from functools import lru_cache


def solve_part_1(data: tuple, start_x: int, start_y: int) -> int:
    beams = set([(start_x + 1, start_y)])

    splits = set()
    while beams:
        x, y = beams.pop()

        if x + 1 >= len(data):
            continue
        if data[x + 1][y] == "^":
            splits.add((x + 1, y))
            beams.add((x + 1, y - 1))
            beams.add((x + 1, y + 1))
        else:
            beams.add((x + 1, y))
    return len(splits)


@lru_cache(maxsize=None)
def solve_part_2(data: tuple[tuple[str]], x: int, y: int) -> int:
    if x + 1 >= len(data):
        return 1
    if data[x + 1][y] == "^":
        return solve_part_2(data, x + 1, y - 1) + solve_part_2(data, x + 1, y + 1)
    return solve_part_2(data, x + 1, y)


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        data = tuple(tuple(x) for x in fp.read().split("\n") if x)

    start_x = 0
    start_y = data[0].index("S")

    return solve_part_1(data, start_x, start_y), solve_part_2(data, start_x, start_y)


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

    assert part_1 == 1541
    assert part_2 == 80158285728929
