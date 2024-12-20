# AOC 2017
# --- Day 9: Stream Processing ---

import re


def solve_part2(data):
    return sum([len(x) - 2 for x in re.findall(r"<[^>]*>", re.sub(r"!.", "", data))])


def solve_part1(data):

    # Removing the !* parts and the garbage
    fixed = re.sub(r"<[^>]*>", "", re.sub(r"!.", "", data))

    level, res = 0, 0
    for i in fixed:
        if i == "{":
            level += 1
        elif i == "}":
            res += level
            level -= 1
    return res


def solve() -> tuple[int, int]:

    with open("input.txt", encoding="utf8") as fp:
        data = fp.read().rstrip()

    return solve_part1(data), solve_part2(data)


if __name__ == "__main__":
    part1, part2 = solve()
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
    assert part1 == 12396
    assert part2 == 6346
