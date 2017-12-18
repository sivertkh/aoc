# --- Day 7: Recursive Circus ---
# part 2 - ok


class Node:

    def __init__(self, name, weight, edges):
        self.name = name
        self.weight = int(weight[1:-1])
        self.edges = edges
        if edges is None:
            self.combined_weight = self.weight
        else:
            self.combined_weight = None

    def __str__(self):
        return "{} {}".format(self.name, self.edges)


def create_tree():
    nodes = {}

    with open('input.txt', 'r') as fp:
        for line in fp:
            n = line.rstrip().split(" ")
            if len(n) > 2:
                edges = [x.rstrip(',') for x in n[3:]]
                nodes[n[0]] = Node(n[0], n[1], edges)
            else:
                # simple node
                nodes[n[0]] = Node(n[0], n[1], None)

    # We do only need to look at nodes with edges.
    ed = [v for k,v in nodes.items() if v.edges is not None]

    root = None
    edges = [x.edges for x in ed]
    flatten = lambda l: [item for sublist in l for item in sublist]

    edges = flatten(edges)

    for n in ed:
        if n.name not in edges:
            root = n.name

    return nodes, root


def calculate_weight(nodes, root, indent):

    if root.edges is None:
#        print("".ljust(indent*4) + "{} ({})".format(root.name, root.combined_weight))
        return root.combined_weight
    else:
        cw = 0
        c = []
        for edge in root.edges:
            e = nodes[edge]

            ew = int(calculate_weight(nodes, e, indent+1))
            cw = cw + ew
            c.append(ew)
        root.combined_weight = cw + root.weight
#        if len(set(c)) != 1:
#            print("FOUND DIFF!")
#        print("".ljust(indent*4) + "{} ({})".format(root.name, root.combined_weight))

        return root.combined_weight

def print_tree(nodes, root, indent):

    print("".ljust(indent*4) + "{} ({})".format(root.name, root.combined_weight))

    if root.edges is not None:
        for edge in root.edges:
            e = nodes[edge]
            print_tree(nodes, e, indent+1)


if __name__ == "__main__":

    nodes, root = create_tree()
    print(calculate_weight(nodes, nodes[root], 0))

    # Quick and dirty.. look at the full tree and find the subtree with problems..
    # Calculate the diff manually..
    #print_tree(nodes, nodes[root], 0)
    root = nodes['kzltfq']
    print_tree(nodes, root, 0)