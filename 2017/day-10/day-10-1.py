# --- Day 10: Knot Hash ---
# part 1 -


knot = [x for x in range(256)]

cur_pos = 0
skip_size = 0
lengths = [187, 254, 0, 81, 169, 219, 1, 190, 19, 102, 255, 56, 46, 32, 2, 216]

knot = [x for x in range(5)]
lengths = [3, 4, 1, 5]

print(knot)
for length in lengths:

    start = cur_pos
    end = cur_pos + length

    if end >= len(knot)-1:
        # Wrapping around

        wrap_size = end - len(knot)-1

        # start is start
        # end is end of list

        part = knot[start:len(knot)] + knot[0:(end % len(knot))]
        part.reverse()

        # Split it..

        knot[start:length(knot)]

        print("-----")
        print(part)
        print("-----")

    else:
        # No wrapping
        part = knot[start:end]
        part.reverse()
        knot[start:end] = part

    cur_pos = cur_pos + length + skip_size
    skip_size = skip_size + 1
    print(knot)
print(knot)
