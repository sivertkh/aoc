# --- Day 21: Fractal Art ---
# part 1 - ok

import numpy as np
import cProfile


def run():

    rules = {}

    with open('input.txt', 'r') as fp:
        for x in fp:
            line = x.rstrip().split(' => ')
            k = "".join([x for x in line[0] if x in '.#'])
            v = [[x for x in y] for y in line[1].split('/')]
            rules[k] = v

    # When searching for a rule to use, rotate and flip the pattern as necessary.
    pattern = np.array([['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']])

    for k in range(5):

        split_size = 0
        if len(pattern) % 2 == 0:
            # split into 2x2 blocs
            split_size = 2
        elif len(pattern) % 3 == 0:
            # split into 3x3 blocs
            split_size = 3
        else:
            print("Error, something is wrong.. len(pattern) is not dividable with 2 or 3")
            exit(1)

        split = len(pattern) // split_size
        # size of the new array is (split_size + 1) * split
        new_size = (split_size+1) * split
        new_array = np.empty((new_size, new_size), dtype=str)

        i_offset = 0
        for i in range(split):
            j_offset = 0
            for j in range(split):
                y = i * split_size
                x = j * split_size
                sub_array = pattern[y:y+split_size,x:x+split_size]

                orign = "".join(sub_array.flatten())
                flip = "".join(np.flip(sub_array, 1).flatten())
                rot90 = np.rot90(sub_array, 1)
                rot90flip = "".join(np.flip(rot90, 1).flatten())
                rot90 = "".join(rot90.flatten())
                rot180 = np.rot90(sub_array, 2)
                rot180flip = "".join(np.flip(rot180, 1).flatten())
                rot180 = "".join(rot180.flatten())
                rot270 = np.rot90(sub_array, 3)
                rot270flip = "".join(np.flip(rot270, 1).flatten())
                rot270 = "".join(rot270.flatten())

                if orign in rules:
                    # id
                    new = rules[orign]
                elif flip in rules:
                    # flip x
                    new = rules[flip]
                elif rot90 in rules:
                    new = rules[rot90]
                elif rot90flip in rules:
                    new = rules[rot90flip]
                elif rot180 in rules:
                    new = rules[rot180]
                elif rot180flip in rules:
                    new = rules[rot180flip]
                elif rot270 in rules:
                    new = rules[rot270]
                elif rot270flip in rules:
                    new = rules[rot270flip]
                else:
                    print("Error: Not found in rules..! ")
                    print("orign: {}".format(orign))
                    exit(1)

                new_array[i_offset:i_offset+split_size+1, j_offset:j_offset+split_size+1] = new
                j_offset = j_offset + split_size + 1

            i_offset = i_offset + split_size + 1

        pattern = new_array

    print(len([x for x in pattern.flatten() if x == '#']))

cProfile.run('run()')
