# --- Day 1: Inverse Captcha ---
# part 2 - ok

with open('./input.txt', 'r') as fp:
    data = [int(x) for x in fp.read().rstrip()]

skip = len(data)/2
l = len(data)
s = 0
for i, v in enumerate(data):
    if v == data[int((i+skip) % l)]:
        s += v

print(s)
