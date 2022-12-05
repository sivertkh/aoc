# --- Day 5: Supply Stacks ---

from collections import deque
from copy import deepcopy


def load_input():
    with open("input.txt") as fp:
        start_pos, moves = fp.read().split("\n\n")
        start_pos = [x for x in start_pos.split("\n")]
        nr_of_positions = int(start_pos[-1].split()[-1])

        tmp_queues = {i: [] for i in range(1, nr_of_positions + 1)}
        for x in start_pos[:-1]:
            for i, r in enumerate(range(1, nr_of_positions * 4, 4)):
                if x[r].isalpha():
                    tmp_queues[i + 1].extend(x[r])
        start_state = {k: deque(reversed(v)) for k, v in tmp_queues.items()}

        moves = [
            [int(z[i]) for i in [1, 3, 5]]
            for z in [x.strip().split(" ") for x in moves.split("\n") if x]
        ]

    return start_state, moves


def solve(start_state, moves):
    part_1_state = start_state
    part_2_state = deepcopy(start_state)

    for n, f, t in moves:
        for _ in range(n):
            part_1_state[t].append(part_1_state[f].pop())
        part_2_state[t].extend(reversed([part_2_state[f].pop() for _ in range(n)]))

    return "".join([v.pop() for v in part_1_state.values()]), "".join(
        [v.pop() for v in part_2_state.values()]
    )


part_1, part_2 = solve(*load_input())
assert part_1 == "SBPQRSCDF"
assert part_2 == "RGLVRCQSB"
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
