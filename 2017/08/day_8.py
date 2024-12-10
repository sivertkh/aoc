# AOC 2017
# --- Day 8: I Heard You Like Registers ---


def get_register_value(name, register):

    if name not in register:
        register[name] = 0

    return register[name]


def solve():
    register = {}

    with open("input.txt", encoding="utf8") as fp:
        inst = [x.rstrip().split() for x in fp.read().split("\n") if x]

    for i in inst:
        reg = i[0]
        instruction = i[1]
        value = int(i[2])

        if_reg = get_register_value(i[4], register)

        if eval("{}{}{}".format(if_reg, i[5], i[6])):
            if instruction == "inc":
                if reg in register:
                    register[reg] = register[reg] + value
                else:
                    register[reg] = 0 + value
            elif instruction == "dec":
                if reg in register:
                    register[reg] = register[reg] - value
                else:
                    register[reg] = 0 - value

    return max([v for k, v in register.items()]), 0


if __name__ == "__main__":
    part1, part2 = solve()
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
