# --- Day 2: I Was Told There Would Be No Math ---
# part 1 - ok

with open('input.txt', 'r') as fp:

    pkgs = [x.rstrip().split("x") for x in fp]


area = 0
for pkg in pkgs:

    l = int(pkg[0])
    w = int(pkg[1])
    h = int(pkg[2])

    la = l*w
    wa = w*h
    ha = h*l

    area += 2*la + 2*wa + 2*ha + min(la, wa, ha)

print(area)
