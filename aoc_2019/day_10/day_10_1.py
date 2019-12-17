# --- Day 10: Monitoring Station ---
# Part 1 - ok

import math


def get_ast_angle(a, b):
    return math.degrees(math.atan2(a[0] - b[0], a[1] - b[1]))


if __name__ == '__main__':
    with open('./input.txt') as fp:
        grid = [list(x) for x in fp.read().split('\n') if x]
    astroids = [(i, j) for i in range(len(grid))
                for j in range(len(grid[0])) if grid[i][j] == '#']
    result = max([len(set([get_ast_angle(f, t) for t in astroids if t != f]))
                  for f in astroids])
    print(f'Day 10 part 1: {result}')
