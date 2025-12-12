"""
AOC 2025
--- Day 12: Christmas Tree Farm ---
"""


def solve() -> int:
    with open("input.txt", encoding="utf-8") as fp:
        data = [x for x in fp.read().split("\n\n") if x]

    trees = []
    for tree in [x for x in data[-1].split("\n") if x]:
        s, p = tree.split(":")
        trees.append([*map(int, s.split("x")), list(map(int, p.split()))])

    return sum([1 for t in trees if sum(t[2]) <= (t[0] // 3) * (t[1] // 3)])


if __name__ == "__main__":
    part_1 = solve()
    assert part_1 == 519
