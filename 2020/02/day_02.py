# --- Day 1: Report Repair ---
from collections import Counter


def is_valid_pw_part1(rule, pw):
    nr, char = rule.split()
    start, end = [int(x) for x in nr.split('-')]
    c = Counter(pw)
    if char in c:
        if c[char] >= start and c[char] <= end:
            return True
    return False


def is_valid_pw_part2(rule, pw):
    nr, char = rule.split()
    first, second = [int(x) for x in nr.split('-')]
    if len([x for x in [pw[first], pw[second]] if x == char]) == 1:
        return True
    return False


with open('./input.txt') as fp:
    pws = [x.rstrip().split(':') for x in fp.readlines()]

print(f'Part 1: {sum([1 for x in pws if is_valid_pw_part1(x[0], x[1])])}')
print(f'Part 2: {sum([1 for x in pws if is_valid_pw_part2(x[0], x[1])])}')
