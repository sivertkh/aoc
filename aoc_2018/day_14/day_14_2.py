# --- Day 14: Chocolate Charts ---
# Part 2 -

from collections import deque
import itertools

recipes = deque([3, 7])

elf_a = 0
elf_b = 1

nr = [8, 8, 0, 7, 5, 1]

count = 0
#nr = [5, 1, 5, 8, 9]
while True:

    if count % 10000 == 0:
        print(count)
    count += 1
    new = recipes[elf_a] + recipes[elf_b]

    # Split into digets
    recipes.extend([int(x) for x in str(new)])

    elf_a += recipes[elf_a] + 1
    elf_b += recipes[elf_b] + 1

    while elf_a >= len(recipes):
        elf_a -= len(recipes)

    while elf_b >= len(recipes):
        elf_b -= len(recipes)

    end = list(recipes)[-len(nr):]

    if end == nr:
        print(len(recipes)-len(nr))
        exit(0)
