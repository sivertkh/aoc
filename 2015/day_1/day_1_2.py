# --- Day 1: Not Quite Lisp ---
# part 2 - ok

with open('input.txt', 'r') as fp:
    instructions = [1 if y == '(' else -1 for y in [list(x) for x in fp][0]]

s = 0
for c,v in enumerate(instructions):
    s += v
    if s < 0:
        print(c+1)
        exit(0)
