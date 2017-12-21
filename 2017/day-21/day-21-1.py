# --- Day 21: Fractal Art ---
# part 1 -

import numpy as np

rules = {}

with open('input-simple.txt', 'r') as fp:
    for x in fp:
        line = x.rstrip().split(' => ')
        k = "".join([x for x in line[0] if x in '.#'])
        v = [[x for x in y] for y in line[1].split('/')]
        rules[k] = v

# When searching for a rule to use, rotate and flip the pattern as necessary.

pattern = np.array([['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']])
#pattern = np.array([['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '15', '16']])


for k in range(2):

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


    split = int(len(pattern) / split_size)

    # size of the new array is (split_size + 1) * split
    new_size = (split_size+1) * split
    tmp = np.zeros((new_size, new_size))

    print("split_size: {}".format(split_size))
    print("split: {}".format(split))
    print("-*-*-*-")
    for i in range(split):
        for j in range(split):

            y = i * split
            x = j * split
            print("****")
            print(pattern[y:y+split_size,x:x+split_size])
            print("****")
            sub_array = pattern[y:y+split_size,x:x+split_size]

            while True:
                # flatten and lookup
                # if no hit, then try rotate and flip



                pass


    print("-*-*-*-")


    # find match in rules

    # in no match try to rotate and flip
    # Only one operation or multiple?

    # combine into new array

    print(i)