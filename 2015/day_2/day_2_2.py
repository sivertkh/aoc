# --- Day 2: I Was Told There Would Be No Math ---
# part 2 - ok

with open('input.txt', 'r') as fp:
    pkgs = [x.rstrip().split("x") for x in fp]

feet = 0
for pkg in pkgs:

    l = int(pkg[0])
    w = int(pkg[1])
    h = int(pkg[2])

    a = [l,w,h]
    a = sorted(a)

    bow = l * w * h
    feet += a[0]*2 + a[1]*2 + bow

print(feet)
