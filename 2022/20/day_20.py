# --- Day 20: Grove Positioning System ---

import itertools as it


def solve(key: int = 1, rounds: int = 1):
    with open("input.txt") as fp:
        data = [int(x) * key for x in fp.readlines()]

    position_values = list(enumerate(data))
    cyclic_list = it.cycle(position_values.copy())
    zero = (data.index(0), 0)

    for _ in range(len(data) * rounds):
        cur = next(cyclic_list)
        old_index = position_values.index(cur)
        position_values.remove(cur)
        new_index = (old_index + cur[1] + len(position_values)) % len(position_values)
        position_values.insert(new_index, cur)

    zero_index = position_values.index(zero)

    return sum(
        [position_values[(zero_index + i) % len((data))][1] for i in [1000, 2000, 3000]]
    )


part_1 = solve()
part_2 = solve(811589153, 10)
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 2203
assert part_2 == 6641234038999
