# --- Day 19: Go With The Flow ---
# Part 1 - ok


def run_program(program, ip_register):

    register = [0 for x in range(6)]
    ip = 0

    while ip < len(program):
        print(register)
        inst = program[ip]
        op = inst[0]
        a = inst[1]
        b = inst[2]
        c = inst[3]

        s = f'ip={ip} {register} {inst}'

        if op == 'addr':
            register[c] = register[a] + register[b]
        elif op == 'addi':
            register[c] = register[a] + b
        elif op == 'mulr':
            register[c] = register[a] * register[b]
        elif op == 'muli':
            register[c] = register[a] * b
        elif op == 'banr':
            register[c] = register[a] & register[b]
        elif op == 'bani':
            register[c] = register[a] & b
        elif op == 'borr':
            register[c] = register[a] | register[b]
        elif op == 'bori':
            register[c] = register[a] | b
        elif op == 'setr':
            register[c] = register[a]
        elif op == 'seti':
            register[c] = a
        elif op == 'gtir':
            if a > register[b]:
                register[c] = 1
            else:
                register[c] = 0
        elif op == 'gtri':
            if register[a] > b:
                register[c] = 1
            else:
                register[c] = 0
        elif op == 'gtrr':
            if register[a] > register[b]:
                register[c] = 1
            else:
                register[c] = 0
        elif op == 'eqir':
            if a == register[b]:
                register[c] = 1
            else:
                register[c] = 0
        elif op == 'eqri':
            if register[a] == b:
                register[c] = 1
            else:
                register[c] = 0
        elif op == 'eqrr':
            if register[a] == register[b]:
                register[c] = 1
            else:
                register[c] = 0

        if register[ip_register] != ip:
            # Jump!
            ip = register[ip_register]
            register[ip_register] = ip

        s += f' {register}'

        # print(s)

        # Move the ip
        ip += 1
        register[ip_register] = ip
    return(register)


def main():
    with open('input.txt') as fp:
        ip_register = int(fp.readline().rstrip('\n').split(' ')[1])
        program = [x.split(' ') for x in fp.read().split('\n') if x]

        for x in program:
            for i in range(1, len(x)):
                x[i] = int(x[i])

    print(run_program(program, ip_register))


if __name__ == "__main__":
    main()
