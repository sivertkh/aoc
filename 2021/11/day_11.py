# --- Day 11: Dumbo Octopus ---

with open("input.txt") as fp:
    energy = [[int(y) for y in x.strip()] for x in fp.readlines()]

flashes = 0
for step in range(500):
    energy = [[y+1 for y in x] for x in energy]

    while any([any([True for y in x if y > 9]) for x in energy]):
        for i in range(len(energy)):
            for j in range(len(energy[0])):
                if energy[i][j] > 9:
                    flashes += 1
                    energy[i][j] = -1
                    # i + 1
                    if i < len(energy)-1:
                        if energy[i+1][j] != -1:
                            energy[i+1][j] += 1
                        # i + 1, j + 1
                        if j < len(energy[0]) - 1 and energy[i+1][j+1] != -1:
                            energy[i+1][j+1] += 1
                        # i + 1, j - 1
                        if j > 0 and energy[i+1][j-1] != -1:
                            energy[i+1][j-1] += 1
                    # i - 1
                    if i > 0:
                        if energy[i-1][j] != -1:
                            energy[i-1][j] += 1
                        # i - 1, j + 1
                        if j < len(energy[0])-1 and energy[i-1][j+1] != -1:
                            energy[i-1][j+1] += 1
                        # i - 1, j - 1
                        if j > 0 and energy[i-1][j-1] != -1:
                            energy[i-1][j-1] += 1
                    # j + 1
                    if j < len(energy[0]) - 1 and energy[i][j+1] != -1:
                        energy[i][j+1] += 1
                    # j - 1
                    if j > 0 and energy[i][j-1] != -1:
                        energy[i][j-1] += 1

    energy = [[0 if y == -1 else y for y in x] for x in energy]
    if all([all([y == 0 for y in x]) for x in energy]):
        print(f"Part 2: {step+1}")
        break

    if step == 99:
        print(f"Part 1: {flashes}")
