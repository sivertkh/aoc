# --- Day 1: The Tyranny of the Rocket Equation ---
# Part 1 - ok

with open('./input.txt') as fp:
    print(sum([(int(x)//3)-2 for x in fp.read().split('\n') if x]))
