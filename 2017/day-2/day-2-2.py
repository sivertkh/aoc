
from itertools import permutations

#with open('./input.txt', 'r') as fp:
#    data = [ [int(x) for x in line.rstrip().split("\t")] for line in fp]

data = [[5, 9, 2, 8],
        [9, 4, 7, 3],
        [3, 8, 6, 5]]


checksum = 0
for x in data:

    for x in 


    checksum = checksum + (max(x) - min(x))


print checksum
