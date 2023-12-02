# AOC 2023
# --- Day 2: Cube Conundrum ---
import functools


def solve():
    part_1 = 0
    part_2 = 0

    with open("input.txt") as fp:
        data = [x for x in fp.readlines() if x]

    bag_max = {"red": 12, "green": 13, "blue": 14}

    for x in data:
        game_possible = True
        game_id, rest = x.split(":")
        game_id = int(game_id.split(" ")[1])

        rounds = [
            [x.strip().split(" ") for x in r.strip().split(",")]
            for r in rest.split(";")
        ]

        round_max = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for round in rounds:
            for sub_round in round:
                if int(sub_round[0]) > bag_max[sub_round[1]]:
                    game_possible = False
                if int(sub_round[0]) > round_max[sub_round[1]]:
                    round_max[sub_round[1]] = int(sub_round[0])

        if game_possible:
            part_1 += int(game_id)

        part_2 += functools.reduce((lambda x, y: x * y), round_max.values())

    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 2377
assert part_2 == 71220
