# --- Day 12: Rain Risk ---


with open('input.txt') as fp:
    instructions = [x.rstrip() for x in fp.readlines()]


ship_direction = 90
dir_x = 0
dir_y = 0

for instruction in instructions:
    direction = instruction[:1]
    length = int(instruction[1:])

    if direction == 'N':
        dir_x += length
    elif direction == 'S':
        dir_x -= length
    elif direction == 'E':
        dir_y += length
    elif direction == 'W':
        dir_y -= length
    elif direction == 'L':
        ship_direction = (ship_direction - length) % 360
    elif direction == 'R':
        ship_direction = (ship_direction + length) % 360
    elif direction == 'F':
        if ship_direction == 0:
            dir_x += length
        elif ship_direction == 180:
            dir_x -= length
        elif ship_direction == 90:
            dir_y += length
        elif ship_direction == 270:
            dir_y -= length

print(f'Part 1: {abs(dir_x) + abs(dir_y)}')

waypoint_x = 1
waypoint_y = 10
pos_x = 0
pos_y = 0

for instruction in instructions:
    direction = instruction[:1]
    length = int(instruction[1:])

    if direction == 'N':
        waypoint_x += length
    elif direction == 'S':
        waypoint_x -= length
    elif direction == 'E':
        waypoint_y += length
    elif direction == 'W':
        waypoint_y -= length
    elif direction == 'L':
        # (x, y) => (y, -x)
        for _ in range(length//90):
            tmp = waypoint_x
            waypoint_x = waypoint_y
            waypoint_y = -tmp
    elif direction == 'R':
        # (x, y) => (-y, x)
        for _ in range(length//90):
            tmp = waypoint_x
            waypoint_x = -waypoint_y
            waypoint_y = tmp

    elif direction == 'F':
        if waypoint_x < 0:
            pos_x -= abs(waypoint_x) * length
        else:
            pos_x += waypoint_x * length

        if waypoint_y < 0:
            pos_y -= abs(waypoint_y) * length
        else:
            pos_y += waypoint_y * length

print(f'Part 2: {abs(pos_x) + abs(pos_y)}')
