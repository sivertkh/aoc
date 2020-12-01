# --- Day 1: No Time for a Taxicab ---
# Status: OK


with open('./input.txt') as fp:
    path = [[x[0], int(x[1:])] for x in fp.read().rstrip().split(', ')]

x_pos = 0
y_pos = 0
facing = 0

for move in path: 

    if move[0] == 'R':
        facing += 90
    else:
        facing -= 90
    facing = facing%360

    if facing == 0:
        y_pos += move[1]
    elif facing == 90:
        x_pos += move[1]
    elif facing == 180:
        y_pos -= move[1]
    else:
        x_pos -= move[1]

print(f"Part 1: {abs(x_pos)+abs(y_pos)}")

x_pos = 0
y_pos = 0
facing = 0
visited = set()

for move in path: 

    if move[0] == 'R':
        facing += 90
    else:
        facing -= 90
    facing = facing%360

    if facing == 0:
        for i in range(1, move[1]+1):
            if (x_pos, y_pos+i) in visited:
                print(f"Part 2: {abs(x_pos)+abs(y_pos+i)}")        
                raise SystemExit
            visited.add((x_pos, y_pos+i))
        y_pos += move[1]
    elif facing == 90:
        for i in range(1, move[1]+1):
            if (x_pos+i, y_pos) in visited:
                print(f"Part 2: {abs(x_pos+i)+abs(y_pos)}")        
                raise SystemExit
            visited.add((x_pos+i, y_pos))
        x_pos += move[1]
    elif facing == 180:
        for i in range(1, move[1]+1):
            if (x_pos, y_pos-i) in visited:
                print(f"Part 2: {abs(x_pos)+abs(y_pos-i)}")        
                raise SystemExit
            visited.add((x_pos, y_pos-i))
        y_pos -= move[1]
    else:
        for i in range(1, move[1]+1):
            if (x_pos-i, y_pos) in visited:
                print(f"Part 2: {abs(x_pos-i)+abs(y_pos)}")        
                raise SystemExit
            visited.add((x_pos-i, y_pos))
        x_pos -= move[1]

