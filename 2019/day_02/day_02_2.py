import sys

# --- Day 2: 1202 Program Alarm ---
# Part 2 - ok


with open('./input.txt') as fp:
    program_input = [int(x) for x in fp.read().split(',') if x]


for noun in range(100):
    for verb in range(100):
        program = program_input.copy()
        program[1] = noun
        program[2] = verb
        ip = 0
        while True:
            opcode = program[ip]
            if opcode == 1:
                program[program[ip+3]] = program[program[ip+1]] + \
                    program[program[ip+2]]
                ip += 4
            elif opcode == 2:
                program[program[ip+3]] = program[program[ip+1]] * \
                    program[program[ip+2]]
                ip += 4
            elif opcode == 99:
                break
            else:
                break
        if program[0] == 19690720:
            print('Found result:')
            print(f'noun: {noun}, verb: {verb}')
            print(100 * noun + verb)
            sys.exit(0)
