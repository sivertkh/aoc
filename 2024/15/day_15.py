# AOC 2024
# --- Day 15: Warehouse Woes ---

import collections as coll
import numpy as np


def gps_sum(m: np.array, t: chr) -> int:
    return sum([x * 100 + y for x, y in zip(*np.where(m == t))])


def solve_part_1(m: np.array, moves: list) -> int:
    robot_x, robot_y = next(zip(*np.where(m == "@")))

    # No need to store the robot on the map
    m[robot_x][robot_y] = "."

    for move in moves:
        match move:
            case "^":
                m_to = m[robot_x - 1][robot_y]
                if m_to == ".":
                    robot_x -= 1
                elif m_to == "O":
                    nr_of_o = 1
                    for i in range(robot_x - 2, 0, -1):
                        if m[i][robot_y] != "O":
                            break
                        nr_of_o += 1
                    if m[robot_x - nr_of_o - 1][robot_y] == ".":
                        m[robot_x - 1][robot_y] = "."
                        m[robot_x - nr_of_o - 1][robot_y] = "O"
                        robot_x -= 1
            case "v":
                m_to = m[robot_x + 1][robot_y]
                if m_to == ".":
                    robot_x += 1
                elif m_to == "O":
                    nr_of_o = 1
                    for i in range(robot_x + 2, len(m)):
                        if m[i][robot_y] != "O":
                            break
                        nr_of_o += 1
                    if m[robot_x + nr_of_o + 1][robot_y] == ".":
                        m[robot_x + 1][robot_y] = "."
                        m[robot_x + nr_of_o + 1][robot_y] = "O"
                        robot_x += 1
            case "<":
                m_to = m[robot_x][robot_y - 1]
                if m_to == ".":
                    robot_y -= 1
                elif m_to == "O":
                    nr_of_o = 1
                    for i in range(robot_y - 2, 0, -1):
                        if m[robot_x][i] != "O":
                            break
                        nr_of_o += 1
                    if m[robot_x][robot_y - nr_of_o - 1] == ".":
                        m[robot_x][robot_y - 1] = "."
                        m[robot_x][robot_y - nr_of_o - 1] = "O"
                        robot_y -= 1
            case ">":
                m_to = m[robot_x][robot_y + 1]
                if m_to == ".":
                    robot_y += 1
                elif m_to == "O":
                    nr_of_o = 1
                    for i in range(robot_y + 2, len(m[0])):
                        if m[robot_x][i] != "O":
                            break
                        nr_of_o += 1
                    if m[robot_x][robot_y + nr_of_o + 1] == ".":
                        m[robot_x][robot_y + 1] = "."
                        m[robot_x][robot_y + nr_of_o + 1] = "O"
                        robot_y += 1

    return gps_sum(m, "O")


def double_map(m: np.array):
    new_map = []
    for l in m:
        tmp = []
        for c in l:
            if c == "O":
                tmp += "[]"
            elif c == "@":
                tmp += "@."
            else:
                tmp += c * 2
        new_map.append(list(tmp))
    return np.array(new_map)


def move_ud(m: np.array, direction, robot_x, robot_y) -> tuple[int, int]:
    d = 1 if direction == "v" else -1

    m_to = m[robot_x + d][robot_y]
    if m_to == ".":
        return robot_x + d, robot_y

    if m_to == "#":
        return robot_x, robot_y

    if m_to in ["[", "]"]:

        boxes = set()
        check_positions = coll.deque([(robot_x + d, robot_y)])
        if m_to == "[":
            check_positions.append((robot_x + d, robot_y + 1))
        else:
            check_positions.append((robot_x + d, robot_y - 1))

        while check_positions:
            x, y = check_positions.popleft()
            cur_s = m[x][y]

            if (x, y, x + d, y, cur_s) in boxes:
                continue

            boxes.add((x, y, x + d, y, cur_s))
            new_to = m[x + d][y]
            if new_to == "#":
                # On of the boxes next to a wall. Stack is immovable.
                return robot_x, robot_y

            elif new_to in ["[", "]"]:
                check_positions.append((x + d, y))
                if new_to == "[":
                    check_positions.append((x + d, y + 1))
                else:
                    check_positions.append((x + d, y - 1))

        moved_from = []
        moved_to = []
        for b in boxes:
            f_x, f_y, t_x, t_y, t = b
            m[t_x][t_y] = t
            moved_from.append((f_x, f_y))
            moved_to.append((t_x, t_y))

        # Fix positions that become empty after the move
        for x, y in [x for x in moved_from if x not in moved_to]:
            m[x][y] = "."

    return robot_x + d, robot_y


def solve_part_2(m: np.array, moves: list) -> int:

    m = double_map(m)
    robot_x, robot_y = next(zip(*np.where(m == "@")))

    # No need to store the robot on the map
    m[robot_x][robot_y] = "."

    for move in moves:
        match move:
            case "^":
                robot_x, robot_y = move_ud(m, "^", robot_x, robot_y)
            case "v":
                robot_x, robot_y = move_ud(m, "v", robot_x, robot_y)
            case "<":
                m_to = m[robot_x][robot_y - 1]
                if m_to == ".":
                    robot_y -= 1
                elif m_to == "#":
                    pass
                elif m_to == "]":
                    nr_of_o = 1
                    for i in range(robot_y - 2, 0, -1):
                        if m[robot_x][i] not in ["[", "]"]:
                            break
                        nr_of_o += 1

                    lookahead = m[robot_x][robot_y - nr_of_o - 1]
                    if lookahead == ".":
                        m[robot_x][robot_y - nr_of_o - 1 : robot_y] = m[robot_x][
                            robot_y - nr_of_o : robot_y + 1
                        ]
                        m[robot_x][robot_y - 1] = "."
                        robot_y -= 1
                    elif lookahead == "#":
                        pass
            case ">":
                m_to = m[robot_x][robot_y + 1]
                if m_to == ".":
                    robot_y += 1
                elif m_to == "#":
                    pass
                elif m_to == "[":
                    nr_of_o = 1
                    for i in range(robot_y + 2, len(m[0])):
                        if m[robot_x][i] not in ["[", "]"]:
                            break
                        nr_of_o += 1

                    lookahead = m[robot_x][robot_y + nr_of_o + 1]
                    if lookahead == ".":
                        m[robot_x][robot_y + 2 : robot_y + nr_of_o + 2] = m[robot_x][
                            robot_y + 1 : robot_y + nr_of_o + 1
                        ]
                        m[robot_x][robot_y + 1] = "."
                        robot_y += 1
                    elif lookahead == "#":
                        pass

    return gps_sum(m, "[")


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        data = [x for x in fp.read().split("\n\n") if x]
        m = np.array([list(x) for x in data[0].split() if x])
        moves = list(data[1].replace("\n", ""))

    return solve_part_1(m.copy(), moves), solve_part_2(m, moves)


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
    assert part_1 == 1463715
    assert part_2 == 1481392
