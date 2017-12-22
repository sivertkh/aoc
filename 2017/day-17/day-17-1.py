# --- Day 17: Spinlock ---
# part 1 -

from collections import deque


buffer = deque()
buffer.append(0)

cur_pos = 0
step = 316

for i in range(1,2018):
    # step step nr of places
    # if it wrap -> move to
    new_pos = cur_pos

    for a in range(step):
        new_pos = new_pos + 1

        if new_pos >= len(buffer):
            new_pos = 0
    # insert i after the current position.
    buffer.insert(new_pos+1, i)
    cur_pos = new_pos+1

print(list(buffer)[cur_pos-4:cur_pos+4])
print(buffer[cur_pos+1])