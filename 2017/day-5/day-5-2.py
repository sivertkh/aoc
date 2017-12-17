# --- Day 5: A Maze of Twisty Trampolines, All Alike ---
# part 2 -

with open('input.txt', 'r') as fp:
    moves = [int(x) for x in fp.read().split('\n')[:-1]]

#moves = [0,3,0,1,-3]

last_pos = 0
position = 0
steps = 0

while True:
    # continue until we get at IndexError..

    inst = moves[position]
    steps = steps + 1

    try:
        # Try to do the jump and update jump value
        position = position + inst
        moves[position]

    except IndexError:
        # Found the exit!!
        print(steps)
        exit(0)

    moves[last_pos] = moves[last_pos] + 1
    last_pos = position
