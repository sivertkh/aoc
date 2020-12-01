# --- Day 5: Alchemical Reduction ---
# Part 2 - ok


def collaps(polymer):
    while True:
        copy = []
        skip = False
        for i in range(len(polymer)-1):
            if skip:
                skip = False
                continue
            diff = abs(ord(polymer[i]) - ord(polymer[i+1]))
            if diff == 32:
                skip = True
                continue
            copy.append(polymer[i])

        if not skip:
            copy.append(polymer[-1])
        if len(copy) < len(polymer):
            polymer = copy
        else:
            break

    return(len(polymer))


if __name__ == "__main__":
    with open('input.txt') as fp:
        polymer = list(fp.read().rstrip('\n'))

    pairs = [(chr(x), chr(x+32)) for x in range(65, 90)]
    shortest = len(polymer)
    for pair in pairs:
        new_polymers = [x for x in polymer if x != pair[0] and x != pair[1]]
        res = collaps(new_polymers)
        if res < shortest:
            shortest = res

    print(shortest)
