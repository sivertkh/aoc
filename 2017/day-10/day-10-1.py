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
    print(knot)
    print("cur_pos: {}".format(cur_pos))
    print("length: {}".format(length))
    print("skip_size: {}".format(skip_size))
    start = cur_pos
    end = cur_pos + length

    if length == 1:
        # Skipping when the length is 1
        print("Skipping length 1")
        pass
    elif end >= len(knot)-1:
        # Wrapping around

        wrap_size = end - len(knot)-1

        # start is start
        # end is end of list

        part = knot[start:len(knot)] + knot[0:(end % len(knot))]
        part.reverse()

        # Split it..

        a = part[0:(end % len(knot))]
#        knot[start:len(knot)] = a

        knot = knot[:start] + a
        #print("a: {}".format(a))
        #print("from {} to {}".format(0,(end % len(knot))))
        #print("knot after a->{}<-".format(knot))

        # part at the end
        b = part[(end % len(knot)):]

        knot = b + knot[(end % len(knot)):]
#        knot[start:len(knot)] = b
        #print("b: {}".format(b))
        #print("from {} to {}".format((end % len(knot)), len(knot)))
        #print("knot after b->{}<-".format(knot))

    else:
        # No wrapping
        print("No wrapping!")
        part = knot[start:end]
        part.reverse()
        knot[start:end] = part

    cur_pos = cur_pos + length + skip_size
    skip_size = skip_size + 1

    cur_pos = (cur_pos % len(knot))
    print(knot)
    print("-----------------")
print(knot)
