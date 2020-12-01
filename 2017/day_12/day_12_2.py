# --- Day 12: Digital Plumber ---
# part 2 - ok


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
    nr_of_grups = 0
    while len(programs) != 0:
        nr_of_grups += 1
        in_group = set()
        start = next(iter(programs.keys()))
        in_group.add(start)
        follow_pipes(start, programs, in_group)

        for g in in_group:
            programs.pop(g, None)
    print(nr_of_grups)
