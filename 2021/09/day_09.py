# --- Day 9: Smoke Basin ---

from collections import Counter

with open("input.txt") as fp:
    sea_map = [[int(y) for y in x.strip()] for x in fp.readlines()]


def merge_basins(basins, old, new):
    #print(f"mergin {old} with {new}")
    res = [[new if x == old else x for x in y] for y in basins]
    return res


total_risk = 0
basins = [['#' if y == 9 else '.' for y in x] for x in sea_map]
current_basin = 0
merges = 0
for i in range(len(sea_map)):
    for j in range(len(sea_map[0])):
        risk = True
        if i < len(sea_map)-1 and sea_map[i][j] >= sea_map[i+1][j]:
            risk = False
        if i > 0 and sea_map[i][j] >= sea_map[i-1][j]:
            risk = False
        if j < len(sea_map[0])-1 and sea_map[i][j] >= sea_map[i][j+1]:
            risk = False
        if j > 0 and sea_map[i][j] >= sea_map[i][j-1]:
            risk = False
        if risk:
            total_risk += sea_map[i][j] + 1

        if sea_map[i][j] == 9:
            current_basin += 1
            continue
        basins[i][j] = str(current_basin)
        if i > 0:
            if sea_map[i-1][j] != 9:
                if basins[i-1][j] != current_basin:
                    basins = merge_basins(basins, basins[i-1][j], basins[i][j],)
                    current_basin = int(basins[i-1][j])
                    merges += 1
                else:
                    basins[i-1][j] = int(current_basin)
        if j > 0:
            if sea_map[i][j-1] != 9:
                if basins[i][j-1] != current_basin:
                    basins = merge_basins(basins, basins[i][j-1], basins[i][j])
                    current_basin = int(basins[i][j-1])
                    merges += 1
                else:
                    basins[i][j-1] = int(current_basin)
    current_basin += 1

print(f"Part 1: {total_risk}")
a = [x[1] for x in Counter([y for x in basins for y in x]).most_common(4) if x[0] != '#']
print(f"Part 2: {a[0]*a[1]*a[2]}")