# --- Day 5: Binary Boarding ---

with open('input.txt') as fp:
    bps = [x.rstrip() for x in fp.readlines()]


def find_pos(path, ch, start, end):
    if not path:
        return start
    half = end - start + 1
    if path[0] == ch:
        return find_pos(path[1:], ch, start, end-half//2)
    return find_pos(path[1:], ch, start+half//2, end)


def seat_number(path):
    return find_pos(list(path[:7]), 'F', 0, 127) * 8 + find_pos(list(path[7:]), 'L', 0, 7)


seats = [seat_number(x) for x in bps]
print(f'Part 1: {max(seats)}')
print(f'Part 2: {set(range(min(seats), max(seats))).difference(set(seats)).pop()}')
