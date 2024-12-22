# AOC 2024
# --- Day 22: Monkey Market ---

import numpy as np


def next_number(secret_number):
    secret_number = (secret_number * 64 ^ secret_number) % 16777216
    secret_number = (secret_number // 32 ^ secret_number) % 16777216
    return (secret_number * 2048 ^ secret_number) % 16777216


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        numbers = [int(x) for x in fp.read().split("\n") if x]

    p1_res = 0
    window_size = 4

    seq = {}
    for number in numbers:

        secret_numbers = [int(str(number)[-1])]

        for _ in range(2000):
            number = next_number(number)
            secret_numbers.append(number % 10)
        p1_res += number

        diffs = np.diff(secret_numbers)

        local_seq = set()
        for i in range(len(diffs) - 4 + 1):
            cur_seq = tuple(diffs[i : i + 4])

            if cur_seq in local_seq:
                # We only store the first occurrence of a sequence.
                continue
            local_seq.add(cur_seq)

            if cur_seq in seq:
                seq[cur_seq] += secret_numbers[i + window_size]
            else:
                seq[cur_seq] = secret_numbers[i + window_size]

    return p1_res, max(seq.values())


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
    assert part_1 == 18525593556
    assert part_2 == 2089
