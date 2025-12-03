"""
AOC 2025
--- Day 3: Lobby ---
"""


def solve_part_1(banks: list[list[int]]) -> int:
    total_joltage = 0

    for bank in banks:
        i = bank.index(max(bank[:-1]))
        total_joltage += int(f"{bank[i]}{max(bank[i + 1 :])}")

    return total_joltage


def max_joltage(cur_nr: list[int], bank: list[int]) -> int:
    if len(bank) == 0:
        if len(cur_nr) == 12:
            return int("".join(map(str, cur_nr)))
        else:
            return -1

    if len(cur_nr) == 12:
        return int("".join(map(str, cur_nr)))

    if len(cur_nr) + len(bank) < 12:
        return -1

    for x in range(9, 0, -1):
        for start_index in [i for i, val in enumerate(bank) if val == x]:
            res = max_joltage(cur_nr + [x], bank[start_index:][1:])

            if res != -1:
                return res

    return -1


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        banks = [[*map(int, list(x))] for x in fp.read().split("\n") if x]

    return solve_part_1(banks), sum([max_joltage([], bank) for bank in banks])


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

    assert part_1 == 17403
    assert part_2 == 173416889848394
