# --- Day 13: Packet Scanners ---
# part 1 - ok

with open('input.txt', 'r') as fp:
    tmp = [f.rstrip().split(': ') for f in fp]
    layers = {int(x[0]): int(x[1]) for x in tmp}

size = int(tmp[-1][0])
pos = [(2*(layers[x] - 1)) if x in layers else -1 for x in range(
    size)]

# simple... the scanner is at position 0 every (2*(len(a) - 1))

severity = 0
for i in range(size):
    cur = pos[i]
    if cur != -1 and i > 0 and i % cur == 0:
        # we skip pos 0 as it does not add to the severity..
        # hit
        severity += layers[i] * i

print(severity)
