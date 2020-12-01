# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
# part 2 - ok

with open('input.txt', 'r') as fp:
    path = list(fp.readline().rstrip())

santa_pos_i = 0
santa_pos_j = 0
robot_pos_i = 0
robot_pos_j = 0

visited = {"0,0": 2}

# santa at even
# robot at odd
for c, step in enumerate(path):
    if step == '^':
        # north i--
        if c % 2 == 0:
            santa_pos_i -= 1
        else:
            robot_pos_i -= 1
    elif step == 'v':
        # south i++
        if c % 2 == 0:
            santa_pos_i += 1
        else:
            robot_pos_i += 1
    elif step == '<':
        # west j--
        if c % 2 == 0:
            santa_pos_j -= 1
        else:
            robot_pos_j -= 1
    elif step == '>':
        # east j++
        if c % 2 == 0:
            santa_pos_j += 1
        else:
            robot_pos_j += 1
    else:
        print("Error, unknown step! {}".format(step))
        exit(1)

    if c % 2 == 0:
        key = "{},{}".format(santa_pos_i, santa_pos_j)
    else:
        key = "{},{}".format(robot_pos_i, robot_pos_j)

    if key in visited:
        visited[key] += 1
    else:
        visited[key] = 1

print(len(visited))