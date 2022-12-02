# --- Day 2: Rock Paper Scissors ---


def load_input():
    with open("input.txt") as fp:
        x = [y.strip().split(" ") for y in fp.readlines()]
    return x

def solve(d):
    part_1 = part_2 = 0

    for x in d:
        match x:
            case [y, "X"]:
                match y:
                    case "A":
                        part_1 += 4
                        part_2 += 3
                    case "B":
                        part_1 += 1
                        part_2 += 1
                    case "C":
                        part_1 += 7
                        part_2 += 2
            case [y, "Y"]:
                match y:
                    case "A":
                        part_1 += 8
                        part_2 += 4
                    case "B":
                        part_1 += 5
                        part_2 += 5
                    case "C":
                        part_1 += 2
                        part_2 += 6
            case [y, "Z"]:
                match y:
                    case "A":
                        part_1 += 3
                        part_2 += 8
                    case "B":
                        part_1 += 9
                        part_2 += 9
                    case "C":
                        part_1 += 6
                        part_2 += 7

    return part_1, part_2


part_1, part_2 = solve(load_input())
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")