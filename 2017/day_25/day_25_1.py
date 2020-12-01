# --- Day 25: The Halting Problem ---
# part 1 - ok


state = 'a'
tape = [0 for x in range(12964419)]
pos = int(len(tape)/2)

for _ in range(12964419):
    if state == 'a':
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
            state = 'b'
        else:
            tape[pos] = 0
            pos += 1
            state = 'f'
    elif state == 'b':
        if tape[pos] == 0:
            #tape[pos] = 0
            pos -= 1
            #state = 'b'
        else:
            #tape[pos] = 1
            pos -= 1
            state = 'c'
    elif state == 'c':
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
            state = 'd'
        else:
            tape[pos] = 0
            pos += 1
            #state = 'c'
    elif state == 'd':
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
            state = 'e'
        else:
            #tape[pos] = 1
            pos += 1
            state = 'a'
    elif state == 'e':
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
            state = 'f'
        else:
            tape[pos] = 0
            pos -= 1
            state = 'd'
    elif state == 'f':
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
            state = 'a'
        else:
            tape[pos] = 0
            pos -= 1
            state = 'e'
    else:
        print("ERROR: Unknown state... {}".format(state))
        exit(1)

print(sum(tape))

# In state B:
