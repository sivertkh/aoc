# --- Day 23: Coprocessor Conflagration ---
# part 1 - ok


with open('input.txt', 'r') as fp:
    program = [x.split(" ") for x in fp.read().split('\n')]

position = 0
register = {chr(c): 0 for c in range(ord('a'), ord('i'))}
jumped = False
muled = 0
while True:

    try:
        instruction = program[position]
    except IndexError:

        print(muled)
        exit(0)

    t = instruction[0]
    last = instruction
    try:
        x = int(instruction[1])
    except ValueError:
        x = register[instruction[1]]

    if len(instruction) == 3:
        try:
            y = int(instruction[2])
        except ValueError:
            y = register[instruction[2]]

    if t == 'set':
        # set X Y
        register[instruction[1]] = y
    elif t == 'sub':
        # sub X Y
        register[instruction[1]] = x - y
    elif t == 'mul':
        # mul X Y
        register[instruction[1]] = x * y
        muled += 1
    elif t == 'jnz':
        # jnz X Y
        # jumps with an offset of the value of Y, but only if the value of X
        # is not zero. (An offset of 2 skips the next instruction, an offset
        # of -1 jumps to the previous instruction, and so on.)

        if x != 0:
            # Do a jump to the left!
            position = position + y
            jumped = True

    if not jumped:
        position = position + 1
    else:
        jumped = False
