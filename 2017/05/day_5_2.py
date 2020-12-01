# --- Day 5: A Maze of Twisty Trampolines, All Alike ---
# Part 2 - ok

with open('input.txt', 'r') as fp:
    moves = [int(x) for x in fp.read().split('\n')[:-1]]

last_pos = 0
position = 0
steps = 0

while True:
    inst = moves[position]
    steps = steps + 1

    try:
        position = position + inst
        moves[position]
    except IndexError:
        # Found the exit!!
        print(steps)
        exit(0)

    if moves[last_pos] >= 3:
        moves[last_pos] = moves[last_pos] - 1
    else:
        moves[last_pos] = moves[last_pos] + 1
    last_pos = position
