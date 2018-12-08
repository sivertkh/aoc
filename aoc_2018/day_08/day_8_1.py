# --- Day 8: Memory Maneuver ---
# Part 1 - ok

nodes = []


def parse(data, start, nr_of_subnodes):
    cur_start = start

    for _ in range(nr_of_subnodes):
        nr_of_edges = data[cur_start]
        nr_of_metadata = data[cur_start+1]

        node = {
            'nr_of_edges': nr_of_edges,
            'nr_of_metadata': nr_of_metadata
        }

        cur_start = cur_start + 2
        if nr_of_edges:
            cur_start = parse(data, cur_start, nr_of_edges)

        if nr_of_metadata:
            node['metadata'] = data[cur_start:cur_start + nr_of_metadata]
            cur_start += nr_of_metadata

        nodes.append(node)
    return cur_start


if __name__ == "__main__":
    with open('input.txt') as fp:
        data = [int(y) for x in fp.read().split(
            '\n') if x for y in x.split(' ')]

    parse(data, 0, 1)
    print(sum([sum(x['metadata']) for x in nodes]))
