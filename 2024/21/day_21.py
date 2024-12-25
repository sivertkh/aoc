# AOC 2024
# --- Day 21: Keypad Conundrum ---

import collections as coll
import functools

NUMPAD_MAPPING = {
    "A": (3, 2),
    "0": (3, 1),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
}

DIRPAD_MAPPING = {
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
    "^": (0, 1),
    "A": (0, 2),
}


@functools.cache
def numpad_paths(start: str, end: str) -> str:
    """Find a possible paths between two numbers on the number pad."""

    start_x, start_y = NUMPAD_MAPPING[start]
    end_x, end_y = NUMPAD_MAPPING[end]

    results = []
    queue = coll.deque([[start_x, start_y, ""]])

    while queue:
        cur_x, cur_y, moves = queue.popleft()

        if cur_x == end_x and cur_y == end_y:
            results.append(moves)
            continue

        if cur_x > end_x:
            queue.append([cur_x - 1, cur_y, moves + "^"])
        elif cur_x < end_x and not (cur_y == 0 and cur_x + 1 == 3):
            queue.append([cur_x + 1, cur_y, moves + "v"])

        if cur_y > end_y and not (cur_x == 3 and cur_y - 1 == 0):
            queue.append([cur_x, cur_y - 1, moves + "<"])
        elif cur_y < end_y:
            queue.append([cur_x, cur_y + 1, moves + ">"])

    return results


@functools.cache
def dirpad_paths(start: str, end: str) -> str:
    """Generate all paths between a start and end key on a direction pad keypad."""

    start_x, start_y = DIRPAD_MAPPING[start]
    end_x, end_y = DIRPAD_MAPPING[end]

    results = []

    queue = coll.deque()
    queue.append([start_x, start_y, ""])

    while queue:
        cur_x, cur_y, moves = queue.popleft()

        if cur_x == end_x and cur_y == end_y:
            results.append(moves)

        if cur_x > end_x and cur_y != 0:
            queue.append([cur_x - 1, cur_y, moves + "^"])
        elif cur_x < end_x:
            queue.append([cur_x + 1, cur_y, moves + "v"])

        if cur_y > end_y and not (cur_x == 0 and cur_y - 1 == 0):
            queue.append([cur_x, cur_y - 1, moves + "<"])
        elif cur_y < end_y:
            queue.append([cur_x, cur_y + 1, moves + ">"])

    return results


@functools.cache
def dirpad_sequences(keys: str, index: int, prev_key: str, cur_path: str) -> list[str]:
    """Generate all paths that creates input on a directional pads."""
    if index == len(keys):
        return [cur_path]

    res = []
    for path in dirpad_paths(prev_key, keys[index]):
        res.extend(
            dirpad_sequences(keys, index + 1, keys[index], cur_path + path + "A")
        )

    return res


@functools.cache
def numpad_sequences(keys: str, index: int, prev_key: str, cur_path: str) -> list[str]:
    """Generate all paths that creates a given input on the numerical pads."""
    if index == len(keys):
        return [cur_path]

    res = []
    for path in numpad_paths(prev_key, keys[index]):
        res.extend(
            numpad_sequences(keys, index + 1, keys[index], cur_path + path + "A")
        )

    return res


@functools.cache
def shortest_sequences_length(keys: str, robot_nr: int) -> int:
    """
    Get the length of the shortest sequence of key presses
    on our control panel, to genera keys through n robots.
    """

    if robot_nr == 0:
        return len(keys)

    split_keys = []
    cur_sub = ""
    for key in keys:
        if key == "A":
            split_keys.append(cur_sub + "A")
            cur_sub = ""
        else:
            cur_sub += key

    return sum(
        min(
            shortest_sequences_length(seq, robot_nr - 1)
            for seq in dirpad_sequences(sub_key, 0, "A", "")
        )
        for sub_key in split_keys
    )


def complexity_sum(numbers: str, robot_nr: int) -> int:
    """Create the sum of the complexity number of each number."""
    return sum(
        [
            min(
                [
                    shortest_sequences_length(s, robot_nr)
                    for s in numpad_sequences(n, 0, "A", "")
                ]
            )
            * int("".join(n[:-1]))
            for n in numbers
        ]
    )


def solve() -> tuple[int, int]:
    with open("input.txt", encoding="utf-8") as fp:
        data = [x for x in fp.read().split("\n") if x]
    return complexity_sum(data, 2), complexity_sum(data, 25)


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
    assert part_1 == 132532
    assert part_2 == 165644591859332
