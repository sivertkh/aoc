# --- Day 8: Handheld Halting ---

with open('input.txt') as fp:
    inst = [x.split() for x in fp.readlines()]

accumulator = 0
visited = set()
ip = 0
changes = {}

while ip < len(inst):

    if ip in visited:
        print(f'Part 1: {accumulator}')
        break
    visited.add(ip)
    i = inst[ip]

    if i[0] == 'acc':
        accumulator += int(i[1])
        ip += 1
    elif i[0] == 'jmp':
        changes[ip] = ['nop', i[1]]
        ip += int(i[1])
    else:
        changes[ip] = ['jmp', i[1]]
        ip += 1


for k, change in changes.items():
    accumulator = 0
    visited = set()
    ip = 0
    loop = False
    old = inst[k]
    inst[k] = change
    while ip < len(inst):

        if ip in visited:
            loop = True
            break
        visited.add(ip)

        i = inst[ip]
        if i[0] == 'acc':
            accumulator += int(i[1])
            ip += 1
        elif i[0] == 'jmp':
            ip += int(i[1])
        else:
            ip += 1

    if not loop:
        print(f'Part 2: {accumulator}')
        break
    inst[k] = old
