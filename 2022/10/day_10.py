# --- Day 10: Cathode-Ray Tube ---

from aocd.models import Puzzle


def draw_pixel(position, sprite_position):
    if position >= sprite_position and position < sprite_position + 3:
        return "#"
    return " "


def solve():
    puzzle = Puzzle(year=2022, day=10)
    data = [x.split(" ") for x in puzzle.input_data.split("\n") if x]

    part_1 = []
    part_2 = [[" " for x in range(40)] for _ in range(6)]
    cycle = local_cycle = register_x = 1

    find_cycles = list(range(20, 221, 40))

    for x in data:
        if cycle in find_cycles:
            part_1.append(cycle * register_x)
        part_2[(cycle - 1) // 40][local_cycle - 1] = draw_pixel(local_cycle, register_x)
        cycle += 1
        local_cycle += 1
        if local_cycle > 40:
            local_cycle = 1

        if x[0] == "addx":
            if cycle in find_cycles:
                part_1.append(cycle * register_x)
            part_2[(cycle - 1) // 40][local_cycle - 1] = draw_pixel(
                local_cycle, register_x
            )
            cycle += 1
            local_cycle += 1
            if local_cycle > 40:
                local_cycle = 1

            register_x += int(x[1])

    part_1 = sum(part_1)
    puzzle.answer_a = part_1
    puzzle.answer_b = "BPJAZGAP"

    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print("Part 2:")
for x in part_2:
    print("".join(x))


assert part_1 == 15140
