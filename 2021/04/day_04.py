# --- Day 4: Giant Squid ---

import sys

with open("input.txt") as fp:
    numbers = fp.readline().strip().split(',')
    boards = [x.split('\n') for x in fp.read().lstrip().split('\n\n')]
    boards = [[x.strip().split() for x in y] for y in boards]

board_all_lines = []

for board in boards:
    all_lines = board
    for i in range(len(board[0])):
        all_lines.append([x[i] for x in board])
    board_all_lines.append(all_lines)

first = True
for number in numbers:
    for board in board_all_lines:
        for line in board:
            if number in line:
                line[line.index(number)] = 'x'

            if len(set(line)) == 1:
                if first:
                    board_sum = sum([sum([int(x) for x in y if x != 'x']) for y in board[:len(board)//2]])
                    print(f"Part1: {board_sum * int(number)}")
                    first = False

                if len(board_all_lines) == 1:
                    board_sum = sum([sum([int(x) for x in y if x != 'x']) for y in board[:len(board)//2]])
                    print(f"Part2: {board_sum * int(number)}")
                    sys.exit(0)

                board_all_lines.pop(board_all_lines.index(board))
                break

print(board_all_lines[0])
