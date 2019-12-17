# --- Day 10: Monitoring Station ---
# Part 2 - ok

import math
import sys


def get_ast_angle(a, b):
    angle = math.degrees(math.atan2(a[0] - b[0], a[1] - b[1]))
    if angle < 0:
        return 360 + angle
    return angle


def get_manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_possible_targets(source, astroids):
    targets = [[a, get_ast_angle(source, a)] for a in astroids if a != source]
    check_targets = {}
    for target in targets:
        if target[1] in check_targets:
            existing = check_targets[target[1]]
            distance_existing = get_manhattan_distance(source, existing)
            distance_target = get_manhattan_distance(source, target[0])
            if distance_target < distance_existing:
                check_targets[target[1]] = target[0]
        else:
            check_targets[target[1]] = target[0]
    return check_targets


if __name__ == '__main__':
    with open('./input.txt') as fp:
        grid = [list(x) for x in fp.read().split('\n') if x]
    astroids = [(i, j) for i in range(len(grid))
                for j in range(len(grid[0])) if grid[i][j] == '#']

    astroids = {f: len(set([get_ast_angle(f, t) for t in astroids if t != f]))
                for f in astroids}
    pos = max(astroids, key=lambda a: astroids[a])

    current_angle = 89.99999
    for i in range(200):
        targets = get_possible_targets(pos, astroids)
        if len(targets) == 0:
            print('No more astroid')
            sys.exit(0)

        targets_lt_angle = [
            x for x in targets.keys() if x > current_angle]

        if len(targets_lt_angle) == 0:
            current_angle = 0
            targets_lt_angle = [
                x for x in targets.keys() if x >= current_angle]
        target = min(targets_lt_angle)
        position = targets[target]
        del astroids[position]

        current_angle = target
        if current_angle >= 360:
            current_angle -= 360

        if i+1 == 200:
            solution = position[1]*100 + position[0]
            print(f'Day 10 part 2: {solution}')
