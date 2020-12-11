

with open('input.txt') as fp:
    a = [x.rstrip() for x in fp.readlines()]
    a = [[y for y in x] for x in a]


def is_seat_occupied(board, x, y):
    if x < 0 or y < 0:
        return 0
    try:
        c = board[x][y]
        if c == '#':
            return 1
    except IndexError:
        return 0
    return 0


def nr_of_occupied_adjacent_seats(board, x, y):
    count = 0
    pos = [(x-1, y-1), (x-1, y), (x-1, y+1),(x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    return sum([is_seat_occupied(board, x[0], x[1]) for x in pos])


def apply_rules_1(board):
    new_board = [x.copy() for x in board]
    for x in range(len(new_board)):
        for y in range(len(new_board[0])):
            if new_board[x][y] == '.':
                continue
            occupied_seats = nr_of_occupied_adjacent_seats(board, x, y)
            if board[x][y] == 'L' and occupied_seats == 0:
                new_board[x][y] = '#'
            elif board[x][y] == '#' and occupied_seats >= 4:
                new_board[x][y] = 'L'
    return new_board


def is_first_seat_in_direction_occupied(board, x, y, direction):
    if direction == 'N':
        if x == 0:
            return 0
        for i in range(x-1, -1, -1):
            if board[i][y] == '#':
                return 1
            elif board[i][y] == 'L':
                return 0
        return 0
    elif direction == 'NE':
        if x == 0:
            return 0
        for i, j in zip(range(x-1, -1, -1), range(y+1, len(board[0]))):
            if board[i][j] == '#':
                return 1
            elif board[i][j] == 'L':
                return 0
        return 0
    elif direction == 'E':
        for i in range(y+1, len(board[0])):
            if board[x][i] == '#':
                return 1
            elif board[x][i] == 'L':
                return 0
        return 0
    elif direction == 'SE':
        for i, j in zip(range(x+1, len(board)), range(y+1, len(board[0]))):
            if board[i][j] == '#':
                return 1
            elif board[i][j] == 'L':
                return 0
        return 0
    elif direction == 'S':
        for i in range(x+1, len(board)):
            if board[i][y] == '#':
                return 1
            elif board[i][y] == 'L':
                return 0
        return 0
    elif direction == 'SW':
        if y == 0:
            return 0
        for i, j in zip(range(x+1, len(board)), range(y-1, -1, -1)):
            if board[i][j] == '#':
                return 1
            elif board[i][j] == 'L':
                return 0
        return 0
    elif direction == 'W':
        if y == 0:
            return 0
        for i in range(y-1, -1, -1):
            if board[x][i] == '#':
                return 1
            elif board[x][i] == 'L':
                return 0
        return 0
    elif direction == 'NW':
        if x == 0 or y == 0:
            return 0
        for i, j in zip(range(x-1, -1, -1), range(y-1, -1, -1)):
            if board[i][j] == '#':
                return 1
            elif board[i][j] == 'L':
                return 0
        return 0


def nr_of_occupied_seen_seats(board, x, y):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    return sum([is_first_seat_in_direction_occupied(board, x, y, d) for d in directions])


def apply_rules_2(board):
    new_board = [x.copy() for x in board]
    for x in range(len(new_board)):
        for y in range(len(new_board[0])):
            if new_board[x][y] == '.':
                continue

            occupied_seats = nr_of_occupied_seen_seats(board, x, y)
            if board[x][y] == 'L' and occupied_seats == 0:
                new_board[x][y] = '#'
            elif board[x][y] == '#' and occupied_seats >= 5:
                new_board[x][y] = 'L'
    return new_board


def runner(board, rule_applier):
    while True:
        new_board = rule_applier(board)
        if new_board == board:
            return new_board
        board = new_board


print(f'Part 1: {sum([1 for x in runner(a, apply_rules_1) for y in x if y == "#"])}')
print(f'Part 2: {sum([1 for x in runner(a, apply_rules_2) for y in x if y == "#"])}')
