# AOC 2024
# --- Day 17: Chronospatial Computer ---

import re

import z3


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


def solve_part_2_rev(program, ans):
    if program == []:
        return ans

    for i in range(8):
        a = ans << 3 | i
        b = a % 8
        b = b ^ 5
        c = a >> b
        b = b ^ 6
        # a = a >> 3 # Skip instruction to get the correct answer directly for the next call.
        b = b ^ c
        if b % 8 == program[-1]:
            s = solve_part_2_rev(program[:-1], a)
            if s:
                return s


def solve_part_2_z3(program):
    o = z3.Optimize()
    s = z3.BitVec("s", 64)
    a = s
    b = 0
    c = 0
    for x in program:
        b = a % 8
        b = b ^ 5
        c = a >> b
        b = b ^ 6
        a = a >> 3
        b = b ^ c
        o.add((b % 8) == x)

    o.add(a == 0)
    o.minimize(s)

    if o.check() == z3.sat:
        return o.model().eval(s)

    return -1


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        registry, program = [x for x in fp.read().split("\n\n") if x]

    program = list(map(int, re.findall(r"-?[0-9]\d*", program)))
    registry = {
        chr(65 + i): int(x) for i, x in enumerate(re.findall(r"-?[0-9]\d*", registry))
    }

    p2_1 = solve_part_2_rev(program, 0)
    p2_2 = solve_part_2_z3(program)
    assert p2_1 == p2_2

    return solve_part_1(registry, program), p2_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == "3,6,3,7,0,7,0,3,0"
assert part_2 == 136904920099226
