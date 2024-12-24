# AOC 2024
# --- Day 24: Crossed Wires ---

import collections as coll
import graphviz


def run_program(wire_state, gates):

    queue = coll.deque(gates)
    while queue:
        cur_gate = queue.popleft()

        if cur_gate[0] not in wire_state or cur_gate[2] not in wire_state:
            queue.append(cur_gate)
            continue

        left_side = wire_state[cur_gate[0]]
        right_side = wire_state[cur_gate[2]]
        match cur_gate[1]:
            case "OR":
                wire_state[cur_gate[3]] = int(left_side or right_side)
            case "AND":
                wire_state[cur_gate[3]] = int(left_side and right_side)
            case "XOR":
                wire_state[cur_gate[3]] = int(left_side != right_side)

    return wire_state


def print_result(wire_state):
    tmp = {k: v for k, v in wire_state.items() if k[0] == "z"}
    tmp = dict(sorted(tmp.items(), reverse=True))
    return int("".join(map(str, tmp.values())), 2)


def print_gates(gates):

    dot = graphviz.Digraph(comment="Wires")
    for gate in gates:
        gate_name = f"{gate[0]} {gate[1]} {gate[2]}"
        dot.node(gate_name, gate[1])

        dot.node(gate[0])
        dot.node(gate[2])
        dot.node(gate[3])

        dot.edge(gate[0], gate_name)
        dot.edge(gate[2], gate_name)
        dot.edge(gate_name, gate[3])

    dot.render("fix-4.gv", view=True)


def solve_part_1(wire_state, gates):
    wire_state = run_program(wire_state, gates)
    return print_result(wire_state)


def solve_part_2():
    """
    Solve part 2 by printing out the full wiring of the gates.

    By looking carefully at the printout we find the 4 errors.

    Error nr 1:
    x11 AND y11 -> qnw
    x11 XOR y11 -> qff

    Error nr 2:
    cts XOR bcd -> qqp
    jcd OR  WDR -> z23

    Error nr 3:
    x16 AND y16 -> z16
    qcr XOR dnf -> pbv

    Error nr 4:
    jdd AND rbm -> z36
    jdd XOR rdm -> fbq
    """

    return ",".join(sorted(["fbq", "pbv", "qff", "qnw", "qqp", "z16", "z23", "z36"]))


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        start, gates = fp.read().split("\n\n")

    wire_state = {}
    for s in start.split("\n"):
        if not s:
            continue
        tmp = s.split(": ")
        wire_state[tmp[0]] = int(tmp[1])

    new_gates = []
    for g in gates.split("\n"):
        if not g:
            continue
        tmp = g.split()
        new_gates.append([tmp[0], tmp[1], tmp[2], tmp[4]])
    gates = new_gates

    return solve_part_1(wire_state.copy(), gates), solve_part_2()


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
assert part_1 == 49430469426918
assert part_2 == "fbq,pbv,qff,qnw,qqp,z16,z23,z36"
