

with open('./input.txt', 'r') as fp:
    data = [ [int(x) for x in line.rstrip().split("\t")] for line in fp]


checksum = 0
for x in data:
    checksum = checksum + (max(x) - min(x))

print(checksum)
