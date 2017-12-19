# --- Day 17: Spinlock ---
# part 1 - ok

from collections import deque

buffer = deque()
buffer.append(0)

cur_pos = 0
step = 316

for i in range(1,50000001):
    # step step nr of places
    # if it wrap -> move to
    new_pos = cur_pos

    if i % 100000 == 0:
        print(i)

    for a in range(step):
        new_pos = new_pos + 1

        if new_pos >= len(buffer):
            new_pos = 0
    # insert i after the current position.
    buffer.insert(new_pos+1, i)
    cur_pos = new_pos+1


for c,v in enumerate(list(buffer)):
    if v == 0:
        print(buffer[c+1])
        print(list(buffer)[c-10:c+10])
        exit(0)
