# --- Day 11: Space Police ---
# Part 2 - ok

from aoc_2019.intcode_runner import IntcodeRunner

grid = [['.' for _ in range(44)] for _ in range(8)]
pos_y = pos_x = 1
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
direction = 0
grid[pos_y][pos_x] = '#'

program_input = IntcodeRunner.read_program_from_file('./input.txt')
program = IntcodeRunner(program_input)
program.run_program()
while not program.halted() or program.program_has_output():
    color = program.get_output()
    turn = program.get_output()

    if color != None and turn != None:
        #        print(f'Output!: color: {color}, turn: {turn}')
        if color == 0:
            grid[pos_y][pos_x] = '.'
        else:
            grid[pos_y][pos_x] = '#'
        if turn == 0:
            direction -= 1
            if direction < 0:
                direction = len(directions)-1
        else:
            direction += 1
            if direction > len(directions) - 1:
                direction = 0
        pos_y += directions[direction][0]
        pos_x += directions[direction][1]

    elif program.waiting():
        if grid[pos_y][pos_x] == '.':
            program.add_input(0)
        else:
            program.add_input(1)
        program.run_program()

for g in grid:
    print(''.join(g))
