# --- Day 18: Duet ---
# part 1 - ok


with open('input.txt', 'r') as fp:
    program = [x.split(" ") for x in fp.read().split('\n')]

position = 0
register = {chr(c): 0 for c in range(ord('a'), ord('z'))}
last_sound = None
jumped = False

while True:

    instruction = program[position]

    type = instruction[0]

    try:
        x = int(instruction[1])
    except ValueError:
        x = register[instruction[1]]

    if len(instruction) == 3:
        try:
            y = int(instruction[2])
        except ValueError:
            y = register[instruction[2]]

    print(instruction)

    if type == 'snd':
        # snd X
        last_sound = x
    elif type == 'set':
        # set X Y
        register[instruction[1]] = y
    elif type == 'add':
        # add X Y
        register[instruction[1]] = x + y
    elif type == 'mul':
        # mul X Y
        register[instruction[1]] = x * y
    elif type == 'mod':
        # mod X Y
        register[instruction[1]] = x % y
    elif type == 'rcv':
        # rcv X
        if x != 0:
            print(last_sound)
            exit(0)

    elif type == 'jgz':
        # jgz X Y

        if x > 0:
            # Do a jump to the left!
            position = position + y
            jumped = True

    if not jumped:
        position = position + 1
    else:
        jumped = False
