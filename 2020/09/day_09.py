# --- Day 9: Encoding Error ---
import itertools

with open('input.txt') as fp:
    numbers = [int(x.strip()) for x in fp.readlines()]

invalid_number = 0
for x in range(25, len(numbers)):
    possible_sums = [sum(x) for x in set(
        itertools.permutations(numbers[x-25:x], 2))]
    if not numbers[x] in possible_sums:
        invalid_number = numbers[x]
        break

print(f'Part 1: {invalid_number}')

start = 0
end = 1
while True:
    cur = sum(numbers[start:end])
    if cur == invalid_number:
        print(f'Part 2: {min(numbers[start:end]) + max(numbers[start:end])}')
        break
    elif cur > invalid_number:
        start += 1
        end = start + 1
    else:
        end += 1
