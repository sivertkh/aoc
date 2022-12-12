# --- Day 11: Monkey in the Middle ---
import copy
import re

import numpy as np
from aocd.models import Puzzle


def parse_input(input_data: str) -> list[dict]:
    monkeys = []
    for x in input_data.split("\n\n"):
        y = x.split("\n")

        monkeys.append(
            {
                "items": [int(y) for y in re.findall("-?\d+", y[1])],
                "operation": y[2].split("=")[1].strip().split(" "),
                "test": int(re.findall("-?\d+", y[3])[0]),
                "do": {
                    True: int(re.findall("-?\d+", y[4])[0]),
                    False: int(re.findall("-?\d+", y[5])[0]),
                },
            }
        )
    return monkeys


def solve_part_1(monkeys: list[dict]) -> int:
    inspections = [0 for _ in range(len(monkeys))]
    for _ in range(20):
        for n, m in enumerate(monkeys):
            for i in m["items"]:
                worry_level = eval(
                    "".join(
                        [str(i) if x == "old" else x for x in m["operation"].copy()]
                    )
                )
                worry_level = worry_level // 3
                monkeys[m["do"][worry_level % m["test"] == 0]]["items"].append(
                    worry_level
                )
                inspections[n] += 1
            m["items"] = []

    inspections.sort()
    return inspections[-1] * inspections[-2]


def solve_part_2(monkeys: list[dict]) -> int:
    inspections = [0 for _ in range(len(monkeys))]

    product_of_divisors = np.prod(np.array([x["test"] for x in monkeys]))

    for _ in range(10000):
        for n, m in enumerate(monkeys):
            for i in m["items"]:
                worry_level = eval(
                    "".join(
                        [str(i) if x == "old" else x for x in m["operation"].copy()]
                    )
                )
                worry_level = worry_level % product_of_divisors
                monkeys[m["do"][worry_level % m["test"] == 0]]["items"].append(
                    worry_level
                )
                inspections[n] += 1
            m["items"] = []

    inspections.sort()
    return inspections[-1] * inspections[-2]


def solve():
    puzzle = Puzzle(year=2022, day=11)
    monkeys_1 = parse_input(puzzle.input_data)
    monkeys_2 = copy.deepcopy(monkeys_1)
    part_1 = solve_part_1(monkeys_1)
    part_2 = solve_part_2(monkeys_2)

    # puzzle.answer_a = part_1
    # puzzle.answer_b = part_2
    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")

assert part_1 == 90294
assert part_2 == 18170818354
