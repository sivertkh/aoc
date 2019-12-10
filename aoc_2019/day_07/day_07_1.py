import sys

import itertools
# --- Day 5: Sunny with a Chance of Asteroids ---
# Part 1 - ok


def adjust_mode(mode_array, nr_param):
    if len(mode_array) == nr_param:
        return mode_array
    missing = [0 for _ in range(nr_param - len(mode_array))]
    return mode_array + missing


with open('./input.txt') as fp:
    program_orign = [int(x) for x in fp.read().split(',') if x]

nr_of_amps = 5
phase_settings = itertools.permutations([x for x in range(nr_of_amps)])
max_output = 0
max_phase = []
for phase_setting in phase_settings:
    phase_setting = list(phase_setting)
    last_output = 0
    for amp in range(nr_of_amps):
        first_input = True
        program = program_orign.copy()
        ip = 0
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
                param_1 = (program[program[ip+1]] if mode[0]
                           == 0 else program[ip+1])
                param_2 = (program[program[ip+2]] if mode[1]
                           == 0 else program[ip+2])
                program[program[ip+3]] = param_1 + param_2
                ip += 4
            elif opcode == 2:
                mode = adjust_mode(mode, 3)
                param_1 = (program[program[ip+1]] if mode[0]
                           == 0 else program[ip+1])
                param_2 = (program[program[ip+2]] if mode[1]
                           == 0 else program[ip+2])
                program[program[ip+3]] = param_1 * param_2
                ip += 4
            elif opcode == 3:
                # Never value mode as we write
                if first_input:
                    program[program[ip+1]] = phase_setting[amp]
                    first_input = False
                else:
                    program[program[ip+1]] = last_output
                ip += 2
            elif opcode == 4:
                mode = adjust_mode(mode, 1)
                output = program[program[ip+1]
                                 ] if mode[0] == 0 else program[ip+1]
                last_output = output
                ip += 2
            elif opcode == 5:
                # Jump if true
                mode = adjust_mode(mode, 2)
                jmp = program[program[ip+1]] if mode[0] == 0 else program[ip+1]
                if jmp > 0:
                    ip = program[program[ip+2]
                                 ] if mode[1] == 0 else program[ip+2]
                else:
                    ip += 3
            elif opcode == 6:
                # Jump if false
                mode = adjust_mode(mode, 2)
                jmp = program[program[ip+1]] if mode[0] == 0 else program[ip+1]
                if jmp == 0:
                    ip = program[program[ip+2]
                                 ] if mode[1] == 0 else program[ip+2]
                else:
                    ip += 3
            elif opcode == 7:
                # less then
                mode = adjust_mode(mode, 2)
                param_1 = program[program[ip+1]
                                  ] if mode[0] == 0 else program[ip+1]
                param_2 = program[program[ip+2]
                                  ] if mode[1] == 0 else program[ip+2]

                if param_1 < param_2:
                    program[program[ip+3]] = 1
                else:
                    program[program[ip+3]] = 0
                ip += 4
            elif opcode == 8:
                # equals
                mode = adjust_mode(mode, 2)
                param_1 = program[program[ip+1]
                                  ] if mode[0] == 0 else program[ip+1]
                param_2 = program[program[ip+2]
                                  ] if mode[1] == 0 else program[ip+2]

                if param_1 == param_2:
                    program[program[ip+3]] = 1
                else:
                    program[program[ip+3]] = 0
                ip += 4
            elif opcode == 99:
                break
            else:
                print('Unknown opcode..')
                sys.exit(1)

    if last_output > max_output:
        max_output = last_output
        max_phase = phase_setting

print(f'max output: {max_output}, with settings {max_phase}')
