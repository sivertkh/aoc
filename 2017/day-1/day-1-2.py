
with open('./input.txt', 'r') as fp:
    data = map(int, fp.read().rstrip())

skip = len(data)/2
l = len(data)

# k = data[(i+skip) % len(data)]


s = 0

for i, v in enumerate(data):

    if v == data[(i+skip) % l]:
        s = s + v

print(s)

