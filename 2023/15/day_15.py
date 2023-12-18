# AOC 2023
# --- Day 15: Lens Library ---


def hash_func(my_string) -> int:
    cur_val = 0
    for x in my_string:
        cur_val = ((cur_val + ord(x)) * 17) % 256
    return cur_val


def solve():
    part_1 = 0
    part_2 = 0

    with open("input.txt") as fp:
        data = fp.readline().strip().split(",")

    boxes = {}
    for x in data:
        part_1 += hash_func(x)

        if "=" in x:
            label, focal = x.split("=")
            pos = hash_func(label)
            if pos in boxes:
                boxes[pos][label] = int(focal)
            else:
                boxes[pos] = {label: int(focal)}
        elif "-" in x:
            label = x[:-1]
            pos = hash_func(label)
            if pos in boxes and label in boxes[pos]:
                del boxes[pos][label]

        else:
            raise ValueError(f"{x} is missing!!")

    for k, v in boxes.items():
        for i, v2 in enumerate(v.values()):
            part_2 += (k + 1) * (i + 1) * v2

    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 510388
assert part_2 == 291774
# assert part_2 ==
