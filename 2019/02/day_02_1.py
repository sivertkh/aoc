# --- Day 2: 1202 Program Alarm ---
# Part 1 - ok


with open('./input.txt') as fp:
    program = [int(x) for x in fp.read().split(',') if x]

program[1] = 12
program[2] = 2

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
        print('Error')
        print(f'Fount opcode: {opcode}')
        break
