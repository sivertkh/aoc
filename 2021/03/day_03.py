# --- Day 3: Binary Diagnostic ---

from collections import Counter

with open("input.txt") as fp:
    numbers = [[k for k in x.strip()] for x in fp.readlines()]

ox_numbers = numbers.copy()
co2_numbers = numbers.copy()
gamma = []
ep = []

for i in range(len(numbers[0])):
    c = Counter([x[i] for x in numbers]).most_common(2)
    gamma.append(c[0][0])
    ep.append(c[1][0])

    if len(ox_numbers) > 1:
        c = Counter([x[i] for x in ox_numbers]).most_common(2)
        if c[0][1] == c[1][1]:
            ox_numbers = [x for x in ox_numbers if x[i] == '1']
        else:
            ox_numbers = [x for x in ox_numbers if x[i] == c[0][0]]

    if len(co2_numbers) > 1:
        c = Counter([x[i] for x in co2_numbers]).most_common(2)
        if c[0][1] == c[1][1]:
            co2_numbers = [x for x in co2_numbers if x[i] == '0']
        else:
            co2_numbers = [x for x in co2_numbers if x[i] == c[1][0]]

gamma = int("".join(gamma),2)
ep = int("".join(ep),2)

print(f"Part 1: {gamma*ep}")

ox_number = int("".join(ox_numbers[0]),2)
co_number = int("".join(co2_numbers[0]),2)

print(f"Part 2: {ox_number * co_number}")