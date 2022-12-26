# --- Day 25: Full of Hot Air ---

from aocd.models import Puzzle


def decimal_to_snafu(number: int) -> str:

    if number == 0:
        return ""

    number_div = number // 5
    number_rest = number % 5

    match number_rest:
        case 0 | 1 | 2:
            return decimal_to_snafu(number_div) + str(number_rest)
        case 3:
            return decimal_to_snafu((number_div) + 1) + "="
        case 4:
            return decimal_to_snafu((number_div) + 1) + "-"


def snafu_to_decimal(snafu_str: str) -> int:
    res = 0

    for i, v in enumerate(reversed(list(snafu_str))):
        match v:
            case "0" | "1" | "2":
                res += int(v) * 5**i
            case "-":
                res += -1 * 5**i
            case "=":
                res += -2 * 5**i
            case _:
                raise ValueError
    return res


def solve():
    puzzle = Puzzle(year=2022, day=25)

    part_1 = 0
    part_2 = 0

    data = [x for x in puzzle.input_data.split("\n") if x]

    part_1 = decimal_to_snafu(sum([snafu_to_decimal(x) for x in data]))

    # puzzle.answer_a = part_1
    # puzzle.answer_b = part_2
    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == "2-212-2---=00-1--102"
# assert part_2 ==
