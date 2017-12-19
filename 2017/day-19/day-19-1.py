# --- Day 19: A Series of Tubes ---
# part 1 -


def follow_path(pos_y, pos_x, direction, tubes):

    result = []
    while True:

        if pos_x is None and pos_y is None:
            # At start.. find start position in the top line
            for c,v in enumerate(tubes[0]):
                if v == '|':
                    # found start
                    pos_x = c
                    pos_y = 0
                    direction = 's'
        else:
            symbol = tubes[pos_y][pos_x]

            #tubes[pos_y][pos_x] = '*'
            #for tube in tubes:
            #    print("".join(tube))
            #tubes[pos_y][pos_x] = symbol

            if symbol == ' ':
                return result

            if symbol != '+':
                # Continuing in the same direction.

                if symbol != '|' and symbol != '-':
                    # Letter or something..
                    result.append(symbol)

                if direction == 'n':
                    pos_y = pos_y - 1
                    direction = 'n'
                elif direction == 's':
                    pos_y = pos_y + 1
                    direction = 's'
                elif direction == 'w':
                    pos_x = pos_x - 1
                    direction = 'w'
                else:
                    pos_x = pos_x + 1
                    direction = 'e'
            else:
                # Changing direction
                if direction == 'w' or direction == 'e':
                    try:
                        n = tubes[pos_y-1][pos_x]
                    except ValueError:
                        n = None

                    if n is not None and n != ' ':
                        pos_y = pos_y - 1
                        direction = 'n'
                    else:
                        # If not north then south
                        pos_y = pos_y + 1
                        direction = 's'
                else:
                    try:
                        w = tubes[pos_y][pos_x-1]
                    except ValueError:
                        w = None

                    if w is not None and w != ' ':
                        pos_x = pos_x - 1
                        direction = 'w'
                    else:
                        # If not east then west
                        pos_x = pos_x + 1
                        direction = 'e'


if __name__ == '__main__':
    with open('input.txt', 'r') as fp:
        tubes = [[x for x in line.rstrip('\n')] for line in fp.readlines()]

    print("".join(follow_path(pos_y=None, pos_x=None, direction=None, tubes=tubes)))
