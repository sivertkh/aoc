"""
AOC 2025
--- Day 6: Trash Compactor ---
"""

from collections import deque
import numpy as np


def solve_part_1(data: np.ndarray, operators: list[str]) -> int:
    total = 0
    for i in range(len(data[0])):
        columns = data[:, i]

        if operators[i] == "*":
            total += np.prod(columns)
        else:
            total += np.sum(columns)

    return int(total)


def solve_part_2(data: np.ndarray, operators: list[str]) -> int:
    total = 0
    operators_deque = deque(operators)
    number_max = len(data[:, 0])

    numbers = []
    for i in range(len(data[0])):
        number = "".join(data[:, i])

        if len(number) == number_max and set(number) == {" "}:
            operator = operators_deque.popleft()
            if operator == "+":
                total += np.sum(numbers)
            else:
                total += np.prod(numbers)
            numbers = []
            continue

        numbers.append(int("".join(number)))

    # Handle the last group of numbers
    operator = operators_deque.popleft()
    if operator == "+":
        total += np.sum(numbers)
    else:
        total += np.prod(numbers)

    return int(total)


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        raw_data = [x for x in fp.read().split("\n") if x]

    operators = raw_data[-1].split()
    raw_data = raw_data[:-1]

    return solve_part_1(
        np.array([list(map(int, x.split())) for x in raw_data]), operators
    ), solve_part_2(np.array([list(x) for x in raw_data]), operators)


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

    assert part_1 == 4583860641327
    assert part_2 == 11602774058280
