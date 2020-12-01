# --- Day 12: Subterranean Sustainability ---
# Part 1 - ok

with open('input.txt') as fp:
    tmp = fp.read().split('\n')
    init_state = list(tmp[0].split(' ')[-1])
    notes = [x.split(' => ') for x in tmp[1:] if x]

# Padd the state
left_pad_size = 20
right_pad_size = 40
left_pad = ['.' for x in range(left_pad_size)]
right_pad = ['.' for x in range(right_pad_size)]
state = left_pad + init_state + right_pad

gen = 20

for i in range(1, gen+1):
    new_state = [x for x in state]
    for j in range(2, len(state)-1):
        current = ''.join(state[j-2:j+3])

        found = False
        for note in notes:
            if note[0] == current:
                new_state[j] = note[1]
                found = True
        if not found:
            new_state[j] = '.'

    state = new_state

    if state[2] == '#' or state[-3] == '#':
        print('Overflow!!')
        exit()

nr = [x for x in range(-left_pad_size, len(state))]
print(sum([nr[k] for k, x in enumerate(state) if x == '#']))
