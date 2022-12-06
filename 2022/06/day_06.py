# --- Day 6: Tuning Trouble ---


def load_input(path):
    with open(path) as fp:
        x = fp.read().strip()
    return x


def find_marker(message: str, window_size: int) -> int:
    for i in range(len(message) - window_size):
        if len(set(message[i : i + window_size])) == window_size:
            return i + window_size


def solve(d):
    return find_marker(d, 4), find_marker(d, 14)


part_1, part_2 = solve(load_input("input.txt"))
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 1598
assert part_2 == 2414
