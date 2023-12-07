# AOC 2023
# --- Day 7: Camel Cards ---

import collections as coll
import functools


def type_of_hand(hand, joker=False):
    if joker and "J" in hand:
        # Only check for joker when we need to.
        rest_hand = "".join([x for x in hand if x != "J"])
        nr_of_jokers = len(hand) - len(rest_hand)
        counter = coll.Counter(rest_hand)
        counts = counter.values()

        match nr_of_jokers:
            case 4 | 5:
                # Five of kind
                return 7
            case 3:
                if len(counts) == 1:
                    # Five of kind 3 J + on pair
                    return 7
                # Four of a kind
                return 6
            case 2:
                if len(counter) == 1:
                    # Five of a kind, 2 J + three of a kind
                    return 7
                elif len(counter) == 2:
                    # Four of a kind, 2 J + one pair
                    return 6
                else:
                    # Three of a kind, 2 J + 3 different cards
                    return 4
            case 1:
                if len(counter) == 1:
                    # 5 of kind, 2 J + tre of kind
                    return 7
                elif len(counter) == 2:
                    # two pairs or 3 + 1...
                    if max(counter.values()) == 3:
                        # Four of a kind
                        return 6
                    # Full house
                    return 5
                elif len(counter) == 3:
                    # Three of kind
                    return 4
                # One pair
                return 2
            case default:
                raise ValueError("WTF")

    counts = coll.Counter(hand).values()

    if 5 in counts:
        # 4 of kind
        return 7

    if 4 in counts:
        # 4 of kind
        return 6

    if 3 in counts and 2 in counts:
        # Full house
        return 5

    if 3 in counts:
        # Three of a kind
        return 4

    if 2 in counts and len(counts) == 3:
        # two pairs
        return 3

    if 2 in counts:
        # One pair
        return 2

    # High card
    return 1


def highest_card_hand(hand_a, hand_b, joker=False):
    if joker:
        values = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    else:
        values = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    a = list(hand_a)
    b = list(hand_b)

    for i in range(len(a)):
        a_val = values.index(a[i])
        b_val = values.index(b[i])

        if a_val == b_val:
            continue

        if a_val < b_val:
            return 1
        elif a_val > b_val:
            return -1

    raise ValueError("Unknown card")


def hand_compare(hand_a, hand_b, joker=False):
    if hand_a[0] == hand_b[0]:
        return 0

    a = type_of_hand(hand_a[0], joker=joker)
    b = type_of_hand(hand_b[0], joker=joker)

    if a < b:
        # B is a better hand type
        return -1
    elif a > b:
        # A is a better hand type
        return 1
    return highest_card_hand(hand_a[0], hand_b[0], joker=joker)


def solve():
    with open("input.txt") as fp:
        s = fp.readlines()

    hands = [x.split() for x in s if x]
    hands = sorted(hands, key=functools.cmp_to_key(hand_compare))
    part_1 = sum([int(hands[x][1]) * (x + 1) for x in range(len(hands))])

    hands = sorted(
        hands, key=functools.cmp_to_key(lambda a, b: hand_compare(a, b, True))
    )
    part_2 = sum([int(hands[x][1]) * (x + 1) for x in range(len(hands))])

    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 249483956
assert part_2 == 252137472
