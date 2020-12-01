# --- Day 8: Memory Maneuver ---
# Part 2 - ok

nodes = []


def parse(data, start, nr_of_subnodes, root=False):
    cur_start = start
    sub_nodes = []

    for _ in range(nr_of_subnodes):
        nr_of_edges = data[cur_start]
        nr_of_metadata = data[cur_start+1]

        node = {
            'nr_of_edges': nr_of_edges,
            'nr_of_metadata': nr_of_metadata,
        }

        cur_start = cur_start + 2
        if nr_of_edges:
            cur_start, edges = parse(data, cur_start, nr_of_edges)
            node['edges'] = edges

        if nr_of_metadata:
            node['metadata'] = data[cur_start:cur_start + nr_of_metadata]
            cur_start += nr_of_metadata
            if nr_of_edges == 0:
                node['score'] = sum(node['metadata'])

        nodes.append(node)
        sub_nodes.append(node)
    if root:
        return 0, node
    return cur_start, sub_nodes


def find_tree_score(root):
    if 'edges' not in root:
        return root['score']
    score = 0
    for edge_nr in root['metadata']:
        if edge_nr <= root['nr_of_edges']:
            score += find_tree_score(root['edges'][edge_nr-1])
    return score


if __name__ == "__main__":
    with open('input.txt') as fp:
        data = [int(y) for x in fp.read().split(
            '\n') if x for y in x.split(' ')]

    cur_start, root = parse(data, 0, 1, root=True)
    print(find_tree_score(root))
