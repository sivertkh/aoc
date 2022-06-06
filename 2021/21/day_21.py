# --- Day 21: Dirac Dice ---

import functools
from typing import List

def inp() -> List[int]:
    with open('input.txt') as fp:
        return [int(x.split(':')[1].strip()) - 1 for x in fp.read().strip().split('\n')]


def part_1(p1_start: int, p2_start:int) -> int: 
    def dice():
        num = 0
        while True:
            yield (num % 100 ) +1
            num += 1

    pos = [p1_start, p2_start]
    score = [0, 0]
    d = dice()
    die_rolls = 0

    while True:
        for i in range(2): 
            move = sum([next(d) for _ in range(3)])
            die_rolls += 3
            new_pos = (pos[i] + move) % 10
            pos[i] = new_pos
            score[i] += new_pos + 1
            if score[i] >= 1000:
                if i == 0:
                    return die_rolls * score[1]
                return die_rolls * score[0]


@functools.cache
def part_2(p1_pos: int, p2_pos: int, p1_score: int = 0, p2_score: int = 0) -> List[int]:
    if p1_score >= 21:
        return 1, 0
    if p2_score >= 21:
        return 0, 1 

    p1_wins = 0
    p2_wins = 0
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                new_p1_pos = (p1_pos + i + j + k) % 10
                new_p1_score = p1_score + new_p1_pos + 1

                # Play for the other player
                new_p2_wins, new_p1_wins = part_2(p2_pos, new_p1_pos, p2_score, new_p1_score)
                p1_wins += new_p1_wins
                p2_wins += new_p2_wins

    return p1_wins, p2_wins

player_pos = inp()
print(f"Part1: {part_1(*player_pos)}")
print(f"Part2: {max(part_2(*player_pos))}")
