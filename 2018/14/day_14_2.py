# --- Day 14: Chocolate Charts ---
# Part 2 - ok

recipes = [3, 7]

elf_a = 0
elf_b = 1

nr = [8, 8, 0, 7, 5, 1]

while True:

    new = recipes[elf_a] + recipes[elf_b]
    recipes.extend([int(x) for x in str(new)])

    elf_a += recipes[elf_a] + 1
    elf_a %= len(recipes)
    elf_b += recipes[elf_b] + 1
    elf_b %= len(recipes)

    if recipes[-len(nr):] == nr: 
        print(len(recipes)-len(nr))
        exit(0)
        
    elif recipes[-len(nr)-1:-1] == nr:
        print(len(recipes)-len(nr)-1)
        exit(0)
