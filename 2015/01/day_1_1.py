# --- Day 1: Not Quite Lisp ---
# part 1 - ok

with open('input.txt', 'r') as fp:
    print(sum([1 if y == '(' else -1 for y in [list(x) for x in fp][0]]))



