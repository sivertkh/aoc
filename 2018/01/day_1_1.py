# --- Day 1: Chronal Calibration ---
# part 1 - ok

with open('./input.txt') as fp:
    print(sum([int(x) for x in fp.read().split('\n') if len(x) != 0]))
