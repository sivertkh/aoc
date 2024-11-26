# AOC 2023
# --- Day 18: Lavaduct Lagoon ---


def shoelace_area(x_list, y_list):
    """
    Use the Shoelace method to calculate the area of a polygon.

    Source: https://www.geodose.com/2021/09/how-calculate-polygon-area-unordered-coordinates-points-python.html
    """
    a1, a2 = 0, 0
    x_list.append(x_list[0])
    y_list.append(y_list[0])

    for j in range(len(x_list) - 1):
        a1 += x_list[j] * y_list[j + 1]
        a2 += y_list[j] * x_list[j + 1]
    l = abs(a1 - a2) / 2
    return l


def solve_part_2(data: list) -> int:

    cur_x, cur_y = 0, 0
    x_pos, y_pos = [0], [0]

    for _, _, color in data:
        steps = int(color[2:-2], 16)
        match int(color[-2]):
            case 3:
                cur_x -= steps
            case 1:
                cur_x += steps
            case 2:
                cur_y -= steps
            case 0:
                cur_y += steps

        x_pos.append(cur_x)
        y_pos.append(cur_y)

    frame = 0
    last_x = x_pos[0]
    last_y = y_pos[0]
    for i in range(1, len(x_pos)):
        frame += abs(last_x - x_pos[i]) + abs(last_y - y_pos[i])
        last_x, last_y = x_pos[i], y_pos[i]

    return int(shoelace_area(x_pos, y_pos) + (frame / 2) + 1)


def solve_part_1(data: list) -> int:
    cur_x, cur_y = 0, 0
    x_pos, y_pos = [0], [0]

    for direction, steps, _ in data:
        steps = int(steps)
        match direction:
            case "U":
                cur_x -= steps
            case "D":
                cur_x += steps
            case "L":
                cur_y -= steps
            case "R":
                cur_y += steps

        x_pos.append(cur_x)
        y_pos.append(cur_y)

    frame = 0
    last_x, last_y = x_pos[0], y_pos[0]
    for i in range(1, len(x_pos)):
        frame += abs(last_x - x_pos[i]) + abs(last_y - y_pos[i])
        last_x = x_pos[i]
        last_y = y_pos[i]

    return int(shoelace_area(x_pos, y_pos) + (frame / 2) + 1)


def solve():
    with open("input.txt", "r", encoding="utf-8") as fp:
        data = [x.strip().split(" ") for x in fp.readlines() if x]

    return solve_part_1(data), solve_part_2(data)


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 42317
assert part_2 == 83605563360288
