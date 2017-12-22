# --- Day 21: Fractal Art ---
# part 1 -

import numpy as np

rules = {}

with open('input.txt', 'r') as fp:
    for x in fp:
        line = x.rstrip().split(' => ')
        k = "".join([x for x in line[0] if x in '.#'])
        v = [[x for x in y] for y in line[1].split('/')]
        rules[k] = v

# When searching for a rule to use, rotate and flip the pattern as necessary.
pattern = np.array([['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']])

for k in range(4):
    print("-*-*-*-")

    split_size = 0
    if len(pattern) % 2 == 0:
        # split into 2x2 blocs
        print("2x2 blocks!")
        split_size = 2
    elif len(pattern) % 3 == 0:
        print("3x3 blocks!")
        # split into 3x3 blocs
        split_size = 3
    else:
        print("Error, something is wrong.. len(pattern) is not dividable with 2 or 3")
        exit(1)

    split = int(len(pattern) / split_size)
    # size of the new array is (split_size + 1) * split
    new_size = (split_size+1) * split
    new_array = np.empty((new_size, new_size), dtype=str)

    print("split_size: {}".format(split_size))
    print("split: {}".format(split))
    i_offset = 0

    for i in range(split):
        j_offset = 0
        for j in range(split):
            y = i * split
            x = j * split
            sub_array = pattern[y:y+split_size,x:x+split_size]


            # there are a total of 8 permutatations: id, rot90, rot180, rot270, flipX, flipX after rot90, flipX after rot180, flipX after rot270

            # Flatten
            flatt = "".join(sub_array.flatten())
            rotate = "".join(np.flip(sub_array, 1).flatten())
            if flatt in rules:
                print("In pattern!")
                new = rules[flatt]
            elif rotate in rules:
                print("In rotate!")
                new = rules[rotate]
            else:

                for a in range(1, 4):
                    rotate = "".join(np.rot90(sub_array, a).flatten())
                    if rotate in rules:
                        print("Found in rotate nr {}".format(a))
                        new = rules[rotate]
                        break
                    flip = "".join(np.flip(np.rot90(sub_array, a), 1).flatten())

                    if flip in rules:
                        print("Fount in fliprot! {}".format(a))
                        new = rules[flip]
                        break

            new_array[i_offset:i_offset+split_size+1, j_offset:j_offset+split_size+1] = new
            j_offset = j_offset + split_size + 1


            #while True:
                # flatten and lookup
                # if no hit, then try rotate and flip
        i_offset = i_offset + split_size + 1

    pattern = new_array

    print("-*-*-*-")

    # find match in rules
    # in no match try to rotate and flip
    # Only one operation or multiple?
    # combine into new array


print(pattern)
print(pattern.flatten())
print(len(pattern.flatten()))

print(len([x for x in pattern.flatten() if x == '#']))
print(len([x for x in pattern.flatten() if x == '.']))
