"""
AOC 2025
--- Day 1: Secret Entrance ---
"""


def move_and_count_hits(pos: int, move: tuple[str, int]) -> tuple[int, int]:
    """Move the wheel and count the nr of times we "click" into zero."""

    hits = 0
    last_pos = pos
    if move[0] == "L":
        pos -= move[1]
    else:
        pos += move[1]

    if pos < 0:
        if pos > -100 and last_pos != 0:
            hits += 1
        else:
            if last_pos == 0:
                hits += abs(pos) // 100
            else:
                hits += ((abs(pos) - 1) // 100) + 1

    elif pos > 100:
        if pos < 200:
            hits += 1
        else:
            if last_pos == 0:
                hits += pos // 100
            else:
                hits += (pos - 1) // 100

    pos = pos % 100
    if pos == 0:
        # Handle landing on zero
        hits += 1

    return pos, hits


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        moves: list[tuple[str, int]] = [
            (x[0], int(x[1:])) for x in fp.read().split("\n") if x
        ]

    pos = 50
    part_1_res, part_2_res = 0, 0
    for x in moves:
        pos, new_hits = move_and_count_hits(pos, x)
        if pos == 0:
            part_1_res += 1
        part_2_res += new_hits

    return part_1_res, part_2_res


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

    assert part_1 == 1023
    assert part_2 == 5899
