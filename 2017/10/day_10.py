# AOC 2024
# --- Day 10: Knot Hash ---

from functools import reduce


def tie_knot(lengths, knot, pos=0, skip_size=0):
    cur_pos = pos

    for length in lengths:
        start = cur_pos
        end = cur_pos + length

        if length == 1:
            pass
        elif end > len(knot) - 1:
            wrap_size = len(knot) - start
            part = knot[start : len(knot)] + knot[0 : (end % len(knot))]
            part.reverse()
            knot[start : len(knot)] = part[:wrap_size]
            knot[0 : (end % len(knot))] = part[wrap_size:]
        else:
            part = knot[start:end]
            part.reverse()
            knot[start:end] = part

        cur_pos += length + skip_size
        skip_size += 1
        cur_pos %= len(knot)

    return knot, cur_pos, skip_size


def create_hash(data):
    knot = [x for x in range(256)]
    cur_pos, skip_size = 0, 0
    lengths = [ord(x) for x in data] + [17, 31, 73, 47, 23]

    for _ in range(64):
        knot, cur_pos, skip_size = tie_knot(lengths, knot, cur_pos, skip_size)

    dense = [
        reduce(lambda x, y: x ^ y, knot[i : i + 16]) for i in range(0, len(knot), 16)
    ]

    return "".join([f"{i:02x}" for i in dense])


def solve() -> tuple[int, int]:

    with open("input.txt", encoding="utf8") as fp:
        raw_data = fp.read().strip()

    lengths = list(map(int, raw_data.split(",")))
    knot, _, _ = tie_knot(lengths, [x for x in range(256)])
    return knot[0] * knot[1], create_hash(raw_data)


if __name__ == "__main__":

    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

    assert part_1 == 13760
    assert part_2 == "2da93395f1a6bb3472203252e3b17fe5"
