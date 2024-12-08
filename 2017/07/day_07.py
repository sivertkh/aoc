# --- Day 7: Recursive Circus ---
# part 2 - ok


class Node:

    def __init__(self, name, weight=None, edges=None):
        self.name = name
        if weight is not None:
            self.weight = int(weight[1:-1])
        else:
            self.weight = None

        self.edges = edges
        self.combined_weight = None

    def __str__(self):
        return f"{self.name} {self.edges}"

    def set_weight(self, weight):
        self.weight = int(weight[1:-1])

    def set_edges(self, edges):
        self.edges = edges

    def tree_weight(self):
        if self.edges is None:
            return self.weight
        else:
            sub_tree_weigth = [edge.tree_weight() for edge in self.edges]
            sub_tree_weigth.append(self.weight)

            self.combined_weight = sum(sub_tree_weigth)

            if len(set(sub_tree_weigth)) != 1:
                print("FOUND DIFF!")

            return sub_tree_weigth

    def print_tree(self, indent=0):
        print("".ljust(indent * 4) + "{} ({})".format(root.name, root.combined_weight))
        if self.edges is not None:
            for edge in self.edges:
                edge.print_tree(indent + 1)


def create_tree():
    nodes = {}

    with open("input.txt", "r") as fp:
        for line in fp:

            n = line.rstrip().split(" ")

            if len(n) > 2:
                edge_ids = [x.rstrip(",") for x in n[3:]]

                edges = []
                for edge_id in edge_ids:
                    if edge_id not in nodes:
                        nodes[edge_id] = Node(edge_id)
                    edges.append(nodes[edge_id])

                if n[0] in nodes:
                    nodes[n[0]].set_weight(n[1])
                    nodes[n[0]].set_edges(edges)
                else:
                    nodes[n[0]] = Node(n[0], n[1], edges)
            else:
                # simple node
                if n[0] not in nodes:

                    nodes[n[0]] = Node(n[0], n[1])
                else:
                    nodes[n[0]].set_weight(n[1])

    # We do only need to look at nodes with edges.
    ed = [v for k, v in nodes.items() if v.edges is not None]

    root = None
    edges = [x.edges for x in ed]

    def flatten(l):
        return [item for sublist in l for item in sublist]

    edges = flatten(edges)

    for n in ed:
        if n.name not in edges:
            root = n.name

    root = nodes[root]
    return nodes, root


if __name__ == "__main__":

    nodes, root = create_tree()
    # print(root.tree_weight())

    # Quick and dirty.. look at the full tree and find the subtree with problems..
    # Calculate the diff manually..
    # print_tree(nodes, nodes[root], 0)
    # root = nodes['yruivis']
    root.print_tree()
