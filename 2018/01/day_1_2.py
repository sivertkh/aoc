# --- Day 1: Chronal Calibration ---
# part 2 - ok

import sys

with open('./input.txt') as fp:
    freq_changes = [int(x) for x in fp.read().split('\n') if len(x) != 0]

vissited = set()
current = 0
vissited.add(current)
while True:
    for change in freq_changes:
        current += change
        if current in vissited:
            print(current)
            sys.exit(0)
        vissited.add(current)
