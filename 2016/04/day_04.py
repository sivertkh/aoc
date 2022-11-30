# --- Day 4: Security Through Obscurity ---

import collections as coll


def load_input() -> list[list[str, int, str]]:
    x = []
    with open("input.txt") as fp:
        for line in fp.readlines():
            data, checksum = line.strip().split("[")
            sector_id = int("".join([y for y in data if y.isnumeric()]))
            name = [y for y in data if y.isalpha() or y == "-"]
            checksum = checksum[:-1]
            x.append([name, sector_id, checksum])
    return x


def create_checksum(data: list[str]) -> str:
    data = [x for x in data if x != "-"]
    # Sort to get ties in alphabetical order.
    # Counter sorts ties by first encountered.
    data.sort()
    c = coll.Counter(data).most_common(5)
    return "".join([x[0] for x in c])


assert create_checksum("aaaaa-bbb-z-y-x") == "abxyz"
assert create_checksum("a-b-c-d-e-f-g-h") == "abcde"
assert create_checksum("not-a-real-room") == "oarel"
assert create_checksum("totally-real-room") != "decoy"


def decipher(data: list[str], sector_id: int) -> str:
    skip = sector_id % 26
    res = []
    for y in data:
        if y == "-":
            if sector_id % 2 == 0:
                res.append("-")
            else:
                res.append(" ")
        else:
            cur_value = ord(y)
            cur_value += skip
            if cur_value > 122:
                cur_value = 97 + cur_value - 122 - 1
            res.append(chr(cur_value))
    return "".join(res)


assert decipher("qzmt-zixmtkozy-ivhz", 343) == "very encrypted name"


def solve(d: list[list[str, int, str]]):
    part_1 = 0
    part_2 = 0
    for x in d:
        if create_checksum(x[0]) == x[2]:
            part_1 += x[1]

            # Assume that we have spaces in the correct string
            if x[1] % 2 != 0:
                decrypted = decipher(x[0], x[1])
                if "northpole" in decrypted:
                    print(f"Found part 20 at {x[1]}")
                    print(decrypted)
                    part_2 = x[1]
    return part_1, part_2


data = load_input()
part_1, part_2 = solve(data) == 158835
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
