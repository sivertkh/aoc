# --- Day 16: Permutation Promenade ---
# part 2


with open('input.txt', 'r') as fp:
    moves = fp.readline().rstrip().split(",")
program = [x for x in 'abcdefghijklmnop']

#moves = ['s1', 'x3/4', 'pe/b']
#program = [x for x in 'abcde']

start = "".join(program)
states = []
print("start program: {}".format("".join(program)))

nr = 10000

# The list is circular and return to the original position after 30 iterations
# We only need to run the dance nr % 30 times

t = nr % 30

for i in range(t):
    for move in moves:

        t = move[:1]
        if t == 's':
            # spin sX
            # Move X elements from the end to the front.
            nr = int(move[1:])

            tmp = program[len(program)-nr:] + program[:len(program)-nr]
            program = tmp

        elif t == 'x':
            # exchange xA/B
            # swap program at position A with B
            ex = [int(x) for x in move[1:].split('/')]

            tmp = program[ex[0]]
            program[ex[0]] = program[ex[1]]
            program[ex[1]] = tmp

        elif t == 'p':
            # partner pA/B
            # Swap programs named A with B
            p = move[1:].split('/')

            a_pos = -1
            b_post = -1
            for c, v in enumerate(program):
                if p[0] == v:
                    a_pos = c
                elif p[1] == v:
                    b_pos = c

            tmp = program[a_pos]
            program[a_pos] = program[b_pos]
            program[b_pos] = tmp
        else:
            print("Unknown move! {}".format(move))
            exit(1)

print("".join(program))
