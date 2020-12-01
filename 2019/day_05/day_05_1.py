import sys

# --- Day 5: Sunny with a Chance of Asteroids ---
# Part 1 - ok


def adjust_mode(mode_array, nr_param):
    if len(mode_array) == nr_param:
        return mode_array
    missing = [0 for _ in range(nr_param - len(mode_array))]
    return mode_array + missing


with open('./input.txt') as fp:
    program = [int(x) for x in fp.read().split(',') if x]

ip = 0
program_input = 1
while True:
    inst = [int(x) for x in str(program[ip])]
    if len(inst) == 1:
        opcode = inst[0]
        mode = []
    else:
        opcode = int(''.join([str(x) for x in inst[-2:]]))
        mode = inst[:-2]
        mode.reverse()
    if opcode == 1:
        mode = adjust_mode(mode, 3)
        param_1 = program[program[ip+1]] if mode[0] == 0 else program[ip+1]
        param_2 = program[program[ip+2]] if mode[1] == 0 else program[ip+2]
        program[program[ip+3]] = param_1 + param_2
        ip += 4
    elif opcode == 2:
        mode = adjust_mode(mode, 3)
        param_1 = program[program[ip+1]] if mode[0] == 0 else program[ip+1]
        param_2 = program[program[ip+2]] if mode[1] == 0 else program[ip+2]
        program[program[ip+3]] = param_1 * param_2
        ip += 4
    elif opcode == 3:
        # Never value mode as we write
        program[program[ip+1]] = program_input
        ip += 2
    elif opcode == 4:
        mode = adjust_mode(mode, 1)
        output = program[program[ip+1]] if mode[0] == 0 else program[ip+1]
        print(output)
        ip += 2
    elif opcode == 99:
        break
    else:
        print('Unknown opcode..')
        sys.exit(1)
