# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
# part 1 - ok
with open('input.txt', 'r') as fp:
    path = list(fp.readline().rstrip())

visited = {}
pos_i = 0
pos_j = 0
visited["0,0"] = 1

for step in path:
    if step == '^':
        # north i--
        pos_i -= 1
    elif step == 'v':
        # south i++
        pos_i += 1
    elif step == '<':
        # west j--
        pos_j -= 1
    elif step == '>':
        # east j++
        pos_j += 1
    else:
        print("Error, unknown step! {}".format(step))
        exit(1)

    key = "{},{}".format(pos_i, pos_j)

    if key in visited:
        visited[key] += 1
    else:
        visited[key] = 1

print(len(visited))