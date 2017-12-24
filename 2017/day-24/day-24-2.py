# --- Day 24: Electromagnetic Moat ---
# part 1 -

import numpy as np


# Find all starts
# recursive search (end when there are no more parts to connect)


def create_bridge(bridge, parts, end, largest, lengths):

    if end is None:
        # At the start. Find at part that contains a 0
        for c, part in enumerate(parts):
            if part[0] == 0:
                new_bridge = list(bridge)
                new_bridge.append(part)
                new_parts = list(parts)
                del new_parts[c]
                create_bridge(new_bridge, new_parts, part[1], largest, lengths)
            elif part[1] == 0:
                new_bridge = list(bridge)
                new_bridge.append(part)
                new_parts = list(parts)
                del new_parts[c]
                create_bridge(new_bridge, new_parts, part[0], largest, lengths)
    else:
        # in bridge
        for c, part in enumerate(parts):

            if part[0] == end:
                new_bridge = list(bridge)
                new_bridge.append(part)
                new_parts = list(parts)
                del new_parts[c]
                create_bridge(new_bridge, new_parts, part[1], largest, lengths)
            elif part[1] == end:
                new_bridge = list(bridge)
                new_bridge.append(part)
                new_parts = list(parts)
                del new_parts[c]
                create_bridge(new_bridge, new_parts, part[0], largest, lengths)
        # At the end.

        largest.append(sum([int(item) for sublist in bridge for item in
                            sublist]))
        lengths.append(len(bridge))
        return


if __name__ == '__main__':
    with open('input.txt', 'r') as fp:
        parts = [[int(y) for y in x.split("/")] for x in fp.read().split('\n')]

    largest = []
    lengths = []
    create_bridge([], parts, None, largest, lengths)

    m = max(lengths)
    mpost = [c for c,v in enumerate(lengths) if v == m]

    print(max([largest[i] for i in mpost]))


