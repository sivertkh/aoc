# --- Day 18: Snailfish ---
import math
import itertools as it


def sn_object(sn):
    res = []
    cur_pos = 0
    while cur_pos < len(sn):
        if sn[cur_pos] in ["[", "]"]:
            res.append(sn[cur_pos])
            cur_pos += 1
        elif sn[cur_pos].isdigit():
            nr = sn[cur_pos]
            nr_pos = cur_pos + 1
            while sn[nr_pos].isdigit():
                nr += sn[nr_pos]
                nr_pos += 1
            res.append(int(nr))
            cur_pos = nr_pos
        else:
            cur_pos += 1
    return res


def exp_sn(sn):
    cur = sn
    level = 0
    pos = 0
    while pos < len(cur):
        match cur[pos]:
            case "[":
                level += 1
            case "]":
                level -= 1
            case _:
                if level >= 5 and isinstance(cur[pos + 1], int):
                    lpos = -1
                    for i in range(pos - 1, 0, -1):
                        if isinstance(cur[i], int):
                            lpos = i
                            break
                    rpos = -1
                    for i in range(pos + 2, len(cur)):
                        if isinstance(cur[i], int):
                            rpos = i
                            break
                    if lpos != -1:
                        cur[lpos] = cur[lpos] + cur[pos]
                    if rpos != -1:
                        cur[rpos] = cur[rpos] + cur[pos + 1]
                    cur = cur[: pos - 1] + [0] + cur[pos + 3 :]
                    return cur
        pos += 1
    return cur


def split_sn(sn):
    cur = sn
    last = []
    while last != cur:
        pos = 0
        last = cur
        while pos < len(cur):
            if isinstance(cur[pos], int) and cur[pos] > 9:
                nr = cur[pos]
                new_pair = ["[", math.floor(nr / 2), math.ceil(nr / 2), "]"]
                cur = cur[:pos] + new_pair + cur[pos + 1 :]
                return cur
            pos += 1
    return cur


def reduce_sn(sn):
    cur = sn
    last = []
    while last != cur:
        last = cur
        last_ex = []
        cur_ex = cur
        while last_ex != cur_ex:
            last_ex = cur_ex
            cur_ex = exp_sn(cur_ex)
        cur = split_sn(cur_ex)
    return cur


def mag(sn):
    while len(sn) > 1:
        new = []
        cur = sn
        pos = 0
        while pos < len(cur):
            x = cur[pos]
            match x:
                case "[":
                    new.append(x)
                case "]":
                    if cur[pos - 1] == "[":
                        new = new[:-1]
                    else:
                        new.append(x)
                case _:
                    if isinstance(cur[pos + 1], int):
                        new_nr = 3 * x + 2 * cur[pos + 1]
                        new.append(new_nr)
                        new.append(cur[pos + 2])
                        pos += 2
                    elif cur[pos + 1] == "]" and cur[pos - 1] == "[":
                        # [x] => x
                        new = new[:-1] + [x]
                        pos += 1
                    else:
                        new.append(x)
            pos += 1
        cur = new
        sn = new

    return sn[0]


def solve(sns):
    cur = sns[0]
    for sn in sns[1:]:
        cur = ["["] + cur + sn + ["]"]
        cur = reduce_sn(cur)
    return mag(cur)


with open("input.txt") as fp:
    sns = [sn_object(sn) for sn in fp.read().strip().split()]

print(f"Part 1: {solve(sns)}")
print(f"Part 2: {max([solve([x, y]) for x, y in it.permutations(sns, 2)])}")
