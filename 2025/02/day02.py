"""
AOC 2025
--- Day 2: Gift Shop ---
"""


def solve_part_1(id_ranges: list[list[int]]) -> int:
    invalid_count = 0

    for r in id_ranges:
        for p_id in range(r[0], r[1] + 1):
            s = str(p_id)
            if s[: len(s) // 2] == s[len(s) // 2 :]:
                invalid_count += p_id

    return invalid_count


def solve_part_2(id_ranges: list[list[int]]) -> int:
    invalid = 0
    for r in id_ranges:
        for p_id in range(r[0], r[1] + 1):
            s = str(p_id)
            if s in (s + s)[1:-1]:
                invalid += p_id
    return invalid


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        id_ranges = [
            [*map(int, x.strip().split("-"))] for x in fp.read().split(",") if x
        ]

    return solve_part_1(id_ranges), solve_part_2(id_ranges)


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

    assert part_1 == 23701357374
    assert part_2 == 34284458938
