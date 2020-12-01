# --- Day 10: Knot Hash ---
# part 2 - ok

from functools import reduce


def tie_knot(lengths, knot=range(256), pos=0, skip_size=0):
    cur_pos = pos
    skip_size = skip_size

    for length in lengths:
        start = cur_pos
        end = cur_pos + length

        if length == 1:
            pass
        elif end > len(knot)-1:
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

    return knot, cur_pos, skip_size


def create_hash(inputs):
    knot = [x for x in range(256)]
    cur_pos = 0
    skip_size = 0

    lengths = [ord(x) for x in inputs] + [17, 31, 73, 47, 23]
    for _ in range(64):
        knot, cur_pos, skip_size = tie_knot(lengths, knot, cur_pos, skip_size)

    # xor
    dense = [reduce(lambda x, y: x ^ y, knot[i:i + 16]) for i in
             range(0, len(knot), 16)]

    hex_hash = ''
    for i in dense:
        hex_hash += "%02x" % i

    return hex_hash


if __name__ == '__main__':

    inputs = "187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216"
    khash = create_hash(inputs)

    print(khash)



