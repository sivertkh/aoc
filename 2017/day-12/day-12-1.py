# --- Day 12: Digital Plumber ---
# part 1 - ok


def follow_pipes(pos, programs, group):
    pipes = programs[pos]
    for pipe in pipes:
        if pipe not in group:
            group.add(pipe)
            follow_pipes(pipe, programs, group)


if __name__ == '__main__':
    with open('input.txt', 'r') as fp:
        s = [f.rstrip().split("<->") for f in fp]
        programs = {int(x[0].rstrip()): [int(y.strip()) for y in x[1:][0].split(','
                                                                     '')] for x in s}

    in_group = set()
    in_group.add(0)
    follow_pipes(0, programs, in_group)

    print(len(in_group))
