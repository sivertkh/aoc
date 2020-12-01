# --- Day 17: Spinlock ---
# part 2 -

from collections import deque

buffer = deque()
buffer.append(0)

step = 316

last = {}
for i in range(1, 50000001):
    buffer.rotate(-step)
    buffer.append(i)

print(buffer[buffer.index(0)+1])

