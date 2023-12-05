# AOC 2023
# --- Day 4: Scratchcards ---

from collections import deque


def solve():
    part_1 = 0
    part_2 = 0

    with open("input.txt") as fp:
        s = fp.readlines()

    card_dict = {}

    for x in s:
        if not x:
            continue
        nr, rest = x.split(":")
        winning, played = rest.strip().split("|")
        nr = int(nr.split()[1].lstrip())
        winning = [int(y) for y in winning.strip().split(" ") if y]
        played = [int(y) for y in played.strip().split(" ") if y]
        hits = [x for x in played if x in winning]
        card_dict[nr] = len(hits)

    part_1 = sum([2 ** (x - 1) for x in card_dict.values() if x])

    cards_left = deque(list(range(1, len(card_dict) + 1)))
    max_card = max(card_dict.keys())
    while cards_left:
        cur = cards_left.pop()
        part_2 += 1
        if card_dict[cur] > 0:
            for i in range(1, card_dict[cur] + 1):
                if i > max_card:
                    continue
                cards_left.append(cur + i)

    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 21105
assert part_2 == 5329815
