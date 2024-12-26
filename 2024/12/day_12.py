# AOC 2024
# --- Day 12: Garden Groups ---

import numpy as np


def find_field(x, y, pos, visited) -> list:
    points = [
        p
        for p in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        if p in pos and p not in visited
    ]

    if not points:
        return [(x, y)]

    visited.extend(points)
    s = [(x, y)]
    for t in [find_field(n_x, n_y, pos, visited) for n_x, n_y in points]:
        s.extend(t)
    return s


def divide_into_fields(data) -> list:
    letters = set()
    for x in [set(list(x)) for x in data]:
        for y in x:
            letters.add(y)

    fields = []
    for l in letters:
        pos = [(x, y) for x, y in zip(*np.where(data == l))]
        groups = []
        while pos:
            x, y = pos[0]
            grp = find_field(x, y, pos, [(x, y)])
            groups.append(grp)
            pos = [x for x in pos if x not in grp]
        fields.append(groups)

    return fields


def get_perimeter_len(group) -> int:
    return sum(
        sum(
            1
            for p in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            if p not in group
        )
        for x, y in group
    )


def solve_part_1(data) -> int:
    return sum(
        sum(len(group) * get_perimeter_len(group) for group in groups)
        for groups in data
    )


def corner_count(group) -> int:
    res = 0
    for point in group:
        x, y = point
        ways = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        n = [w for w in ways if w in group]
        match len(n):
            case 0:
                res += 4
            case 1:
                res += 2
            case 2:
                if n not in [[(x - 1, y), (x + 1, y)], [(x, y - 1), (x, y + 1)]]:
                    res += 1
                    if (
                        all([t in n for t in [(x - 1, y), (x, y - 1)]])
                        and (x - 1, y - 1) not in group
                    ):
                        res += 1
                    elif (
                        all([t in n for t in [(x + 1, y), (x, y - 1)]])
                        and (x + 1, y - 1) not in group
                    ):
                        res += 1
                    elif (
                        all([t in n for t in [(x - 1, y), (x, y + 1)]])
                        and (x - 1, y + 1) not in group
                    ):
                        res += 1
                    elif (
                        all([t in n for t in [(x + 1, y), (x, y + 1)]])
                        and (x + 1, y + 1) not in group
                    ):
                        res += 1
            case 3:
                points = []
                if (x - 1, y) not in n:
                    points = [(x + 1, y - 1), (x + 1, y + 1)]
                elif (x + 1, y) not in n:
                    points = [(x - 1, y - 1), (x - 1, y + 1)]
                elif (x, y - 1) not in n:
                    points = [(x - 1, y + 1), (x + 1, y + 1)]
                elif (x, y + 1) not in n:
                    points = [(x - 1, y - 1), (x + 1, y - 1)]
                res += sum(1 for p in points if p not in group)
            case 4:
                points = [
                    (x - 1, y - 1),
                    (x - 1, y + 1),
                    (x + 1, y - 1),
                    (x + 1, y + 1),
                ]
                res += sum(1 for p in points if p not in group)
    return res


def solve_part_2(data) -> int:
    return sum(
        sum(len(group) * corner_count(group) for group in groups) for groups in data
    )


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        data = np.array([list(x) for x in fp.read().split("\n") if x])
    data = divide_into_fields(data)
    return solve_part_1(data), solve_part_2(data)


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
    assert part_1 == 1533024
    assert part_2 == 910066
