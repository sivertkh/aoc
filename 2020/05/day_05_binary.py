# --- Day 5: Binary Boarding ---
import re

with open('input.txt') as fp:
    bps = [x.rstrip() for x in fp.readlines()]

seats = [int(''.join(map(lambda y: '0' if y in ['F', 'L'] else '1', x)), 2) for x in bps]
print(f'Part 1: {max(seats)}')
print(f'Part 2: {set(range(min(seats), max(seats))).difference(set(seats)).pop()}')
