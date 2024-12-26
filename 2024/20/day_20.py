# AOC 2024
# --- Day 20: Race Condition ---

import numpy as np


def generate_points_in_manhattan_square(x: int, y: int, r: int) -> list:
    """Generates all positive points with a manhattan distance of at least r for a point (x,y).

    Modified version of https://stackoverflow.com/a/75129338
    """

    points = []
    for t in range(2, r + 1):
        for offset in range(t):
            inverse_offset = t - offset
            points.extend(
                [
                    (x + offset, y + inverse_offset),
                    (x + inverse_offset, y - offset),
                    (x - offset, y - inverse_offset),
                    (x - inverse_offset, y + offset),
                ]
            )
    return [p for p in points if p[0] >= 0 and p[1] >= 0]


def solve_part_1(dots: dict):
    res = 0
    for k, v in dots.items():
        x, y = k
        for m in [m for m in generate_points_in_manhattan_square(x, y, 2) if m in dots]:
            if v < dots[m]:
                speed = dots[m] - 2 - v
                if speed >= 100:
                    res += 1

    return res


def solve_part_2(dots: dict):
    res = 0
    for k, v in dots.items():
        x, y = k
        for m in [
            m for m in generate_points_in_manhattan_square(x, y, 20) if m in dots
        ]:
            if v < dots[m]:
                cheat_len = abs(x - m[0]) + abs(y - m[1])
                speed = dots[m] - cheat_len - v
                if speed >= 100:
                    res += 1
    return res


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        data = np.array([list(x.strip()) for x in fp.read().split("\n") if x])

    s_x, s_y = next(zip(*np.where(data == "S")))
    e_x, e_y = next(zip(*np.where(data == "E")))

    data[s_x][s_y] = "."
    data[e_x][e_y] = "."

    dots = list(zip(*np.where(data == ".")))

    new_dots = {}
    cur_x, cur_y = s_x, s_y
    path = 1
    visited = set()

    while True:
        x, y = cur_x, cur_y
        visited.add((x, y))

        move = [
            a
            for a in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            if a in dots and a not in visited
        ]
        if len(move) == 0:
            new_dots[(cur_x, cur_y)] = path
            # Found end
            break
        next_x, next_y = move[0]
        new_dots[(cur_x, cur_y)] = path
        path += 1
        cur_x, cur_y = next_x, next_y

    return solve_part_1(new_dots), solve_part_2(new_dots)


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
    assert part_1 == 1415
    assert part_2 == 1022577
