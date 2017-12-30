# --- Day 13: Packet Scanners ---
# part 2 - ok


# simple... the scanner is at position 0 every (2*(len(a) - 1))
def find_path(delay, pos):
    for i in range(size):
        cur = pos[i]
        if cur != -1 and ((delay+i) % cur) == 0:
            # hit
            return False
    return True


if __name__ == '__main__':

    with open('input.txt', 'r') as fp:
        tmp = [f.rstrip().split(': ') for f in fp]
        layers = {int(x[0]): int(x[1]) for x in tmp}

    size = int(tmp[-1][0])+1
    pos = [(2*(layers[x] - 1)) if x in layers else -1 for x in range(size)]

    i = 0
    while True:
        if find_path(i, pos):
            print(i)
            break
        i += 1
