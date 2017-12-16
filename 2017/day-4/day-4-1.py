

with open('input.txt', 'r') as fp:
    pp = [[s for s in line.split(" ")] for line in fp]

valid = 0
for x in pp:
    s = set(x)

    if len(s) == len(x):
        valid = valid + 1
    else:
        print("not valid!!")

print(valid)
