# --- Day 11: Hex Ed ---
# part 2 - ok

# A hex tile has 6 neighbors. This can be modeled by a matrix where the odd
# columns are shifted half a row. From stackowerflow 2334629
#
#  ___     ___       ___ ___ ___
# |   |___|   |     |   | n |   |
# |___| n |___|     |___|___|___|
# | nw|___|ne |     | nw| c |ne |
# |___| c |___|     |___|___|___|
# | sw|___|se |     | sw| s |se |
# |___| s |___|     |___|___|___|
#     |___|   |
#
#  ___     ___
# |   |___| n |___|     ___ ___ ___
# |___| nw|___|ne |    | nw| n |ne |
# |   |___| c |___|    |___|___|___|
# |___| sw|___|se |    | sw| c |se |
# |   |___| s |___|    |___|___|___|
# |___|   |___|   |    |   | s |   |
#     |___|   |___|    |___|___|___|


def find_max_distance():

    with open('input.txt', 'r') as fp:
        steps = [s for s in fp.read().rstrip().split(",")]

    pos_i = 0
    pos_j = 0

    largest_dist = 0

    for step in steps:

        if step == 'n':
            # n(i-1, j)
            pos_i -= 1
            pos_j = pos_j
        elif step == 's':
            # s(i+1, j)
            pos_i += 1
            pos_j = pos_j

        elif pos_j % 2 == 0:
            if step == 'ne':
                # ne(i-1, j+1)
                pos_i -= 1
                pos_j += 1
            elif step == 'se':
                # se(i, j+1)
                pos_i = pos_i
                pos_j += 1

            elif step == 'sw':
                # sw(i, j-1)
                pos_i = pos_i
                pos_j -= 1
            elif step == 'nw':
                # nw(i-1, j-1),
                pos_i -= 1
                pos_j -= 1
        else:
            if step == 'ne':
                # ne(i, j+1)
                pos_i = pos_i
                pos_j += 1
            elif step == 'se':
                # se(i+1, j+1)
                pos_i += 1
                pos_j += 1
            elif step == 'sw':
                # sw(i+1, j-1)
                pos_i += 1
                pos_j -= 1
            elif step == 'nw':
                # nw(i, j-1)
                pos_i = pos_i
                pos_j -= 1

        distance = steps_from_start(pos_i, pos_j)

        if distance > largest_dist:
            largest_dist = distance
    print(largest_dist)


def steps_from_start(pos_i, pos_j):

    steps = 0

    if pos_i < 0 > pos_j:
        # move in the se direction
        while pos_j != 0:
            steps += 1
            if pos_j % 2 == 0:
                # se(i, j+1)
                pos_i = pos_i
                pos_j += 1
            else:
                # se(i+1, j+1)
                pos_i += 1
                pos_j += 1

    elif pos_i < 0 < pos_j:
        # move in the sw direction
        while pos_j != 0:
            steps += 1
            if pos_j % 2 == 0:
                # sw(i, j-1)
                pos_i = pos_i
                pos_j -= 1
            else:
                # sw(i+1, j-1)
                pos_i += 1
                pos_j -= 1

    elif pos_i > 0 > pos_j:
        # move in the ne direction
        while pos_j != 0:
            steps += 1
            if pos_j % 2 == 0:
                # ne(i-1, j+1)
                pos_i -= 1
                pos_j += 1
            else:
                # ne(i, j+1)
                pos_i = pos_i
                pos_j += 1

    elif pos_i > 0 < pos_j:
        # move in the nw direction
        while pos_j != 0:
            steps += 1
            if pos_j % 2 == 0:
                pass
                # nw(i-1, j-1),
                pos_i -= 1
                pos_j -= 1
            else:
                # nw(i, j-1)
                pos_i = pos_i
                pos_j -= 1

    steps += abs(pos_i)
    return steps


if __name__ == '__main__':
    find_max_distance()
