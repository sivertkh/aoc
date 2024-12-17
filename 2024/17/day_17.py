# AOC 2024
# --- Day 17: Chronospatial Computer ---

import re


def get_combo_value(registry, value):

    if value <= 3:
        return value
    if value == 4:
        return registry["A"]
    if value == 5:
        return registry["B"]
    if value == 6:
        return registry["C"]
    if value == 7:
        raise NotImplementedError


def solve_part_1(registry, prog):
    res = 0

    output_buffer = []

    ip = 0
    while ip < len(prog):
        inst = prog[ip]
        match inst:
            case 0:
                numerator = registry["A"]
                combo = get_combo_value(registry, prog[ip + 1])
                denominator = 2**combo
                registry["A"] = numerator // denominator
                ip += 2
            case 1:
                literal = prog[ip + 1]
                # Registry is larger then 3 bit.
                registry["B"] = literal ^ registry["B"]
                ip += 2
            case 2:
                combo = get_combo_value(registry, prog[ip + 1])
                registry["B"] = combo % 8
                ip += 2
            case 3:
                if registry["A"] != 0:
                    literal = prog[ip + 1]
                    ip = literal
                else:
                    ip += 2
            case 4:
                registry["B"] = registry["B"] ^ registry["C"]
                ip += 2
            case 5:
                combo_value = get_combo_value(registry, prog[ip + 1])
                res = combo_value % 8
                output_buffer.append(str(res))
                ip += 2
            case 6:
                numerator = registry["A"]
                combo = get_combo_value(registry, prog[ip + 1])
                denominator = 2**combo
                registry["B"] = numerator // denominator
                ip += 2
            case 7:
                numerator = registry["A"]
                combo = get_combo_value(registry, prog[ip + 1])
                denominator = 2**combo
                registry["C"] = numerator // denominator
                ip += 2

    return ",".join(output_buffer)


def solve_part_2(registry, program):
    pass
    # for x in program:
    #     b = a % 8
    #     b = b ^ 5
    #     c = a / (1 << b)
    #     b = b ^ c
    #     b = b ^ 6
    #     a = a / (1 << 3)
    #     (b % 8) == x


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        a = [x for x in fp.read().split("\n\n") if x]

        reg, prog = a[0], a[1]

        prog = list(map(int, re.findall(r"-?[0-9]\d*", prog)))

        registry = {}
        for i, x in enumerate(re.findall(r"-?[0-9]\d*", reg)):
            registry[chr(65 + i)] = int(x)

    # print(prog)
    # print(registry)

    data = []

    return solve_part_1(registry, prog), solve_part_2(registry, prog)


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == "3,6,3,7,0,7,0,3,0"
# assert part_2 ==
