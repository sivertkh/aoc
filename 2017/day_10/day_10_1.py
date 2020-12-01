# --- Day 10: Knot Hash ---
# part 1 - ok

knot = [x for x in range(256)]

cur_pos = 0
skip_size = 0
lengths = [187, 254, 0, 81, 169, 219, 1, 190, 19, 102, 255, 56, 46, 32, 2, 216]

for length in lengths:
    start = cur_pos
    end = cur_pos + length

    if length == 1:
        pass
    elif end >= len(knot)-1:
        wrap_size = len(knot) - start
        part = knot[start:len(knot)] + knot[0:(end % len(knot))]
        part.reverse()

        knot[start:len(knot)] = part[:wrap_size]
        knot[0:(end % len(knot))] = part[wrap_size:]

    else:
        # No wrapping
        part = knot[start:end]
        part.reverse()
        knot[start:end] = part

    cur_pos = cur_pos + length + skip_size
    skip_size = skip_size + 1
    cur_pos = (cur_pos % len(knot))

print(knot[0] * knot[1])
