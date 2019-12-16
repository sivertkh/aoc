# --- Day 15: Oxygen System ---
# Part 1 -

from aoc_2019.intcode_runner import IntcodeRunner

with open('./input.txt') as fp:
    program_input = [int(x) for x in fp.read().split(',') if x]

program = IntcodeRunner(program_input, break_on_output=True, debug=True)

program.run_program()
while not program.halted():

    if program.waiting():
        # Try all possible paths..
        program.add_input(1)
        program.run_program()
    elif program.got_output():
        output = program.get_output()
        print(f'Output: {output}')
        program.run_program()
