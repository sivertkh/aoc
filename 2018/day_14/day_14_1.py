# --- Day 14: Chocolate Charts ---
# Part 1 - ok

recipes = [3, 7]
elf_a = 0
elf_b = 1
nr = 880751

while len(recipes) < 10+nr:

    new = recipes[elf_a] + recipes[elf_b]
    recipes.extend([int(x) for x in str(new)])

    elf_a += recipes[elf_a] + 1
    elf_a %= len(recipes)
    elf_b += recipes[elf_b] + 1
    elf_b %= len(recipes)

print(''.join([str(x) for x in list(recipes)[nr:nr+10]]))
