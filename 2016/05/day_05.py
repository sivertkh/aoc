# --- Day 5: How About a Nice Game of Chess? ---

from hashlib import md5


def solve(d):
    res_part_1 = []
    res_part_2 = [None for _ in range(8)]
    i = 0
    # Part 2 will always use more iterations
    while None in res_part_2:
        h = md5(f"{d}{i}".encode()).hexdigest()
        try:
            if int(h[:5]) == 0:
                if len(res_part_1) < 8:
                    res_part_1.append(h[5])
                pos = int(h[5], 16)
                if pos < 8 and not res_part_2[pos]:
                    res_part_2[pos] = h[6]
        except ValueError:
            pass
        i += 1

    return "".join(res_part_1), "".join(res_part_2)


data = "reyedfim"

part_1, part_2 = solve(data)

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
