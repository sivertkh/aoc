# --- Day 20: A Regular Map ---
# Part 2 - ok

from collections import deque
import networkx


def main():

    with open('input.txt') as fp:
        mapex = list(fp.read().rstrip('\n'))[1:-1]

    graf = networkx.Graph()
    pos_x = 0
    pos_y = 0
    stack = deque()

    for c in mapex:
        if c == '(':
            stack.append((pos_x, pos_y))
        elif c == '|':
            pos_x, pos_y = stack[-1]
        elif c == ')':
            pos_x, pos_y = stack.pop()
        else:
            from_x = pos_x
            from_y = pos_y
            if c == 'E':
                pos_x += 1
            elif c == 'S':
                pos_y += 1
            elif c == 'W':
                pos_x -= 1
            else:
                pos_y -= 1

            graf.add_edge((from_x, from_y), (pos_x, pos_y))

    lengths = networkx.algorithms.shortest_path_length(graf, (0, 0))
    print(sum([1 for x in lengths.values() if x >= 1000]))


if __name__ == "__main__":

    main()
