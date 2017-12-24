#
# part 1 -

with open('input.txt', 'r') as fp:
    parts = [x.split(" ") for x in fp.read().split('\n')]

print()

# Find all starts
# recursive search (end when there are no more parts to connect)
