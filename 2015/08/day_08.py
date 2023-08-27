# --- Day 8: Matchsticks ---
import ast


def main():
    with open("input.txt") as fp:
        data = [x.rstrip() for x in fp.readlines() if x]

        part_1 = sum([len(x) - len(ast.literal_eval(x)) for x in data])

        # Add two for the new "" at each end
        part_2 = sum([2 + len(x) + x.count('"') + x.count("\\") - len(x) for x in data])

    assert part_1 == 1342
    assert part_2 == 2074

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()