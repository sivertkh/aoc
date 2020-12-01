# --- Day 15: Beverage Bandits ---
# Part 1 - ok
# Part 2 - ok

import networkx as nx


class NetElf(object):

    def __init__(self, board_file, elf_ap=3):
        self.elf_ap = elf_ap
        self.create_board_graph(board_file)
        self.elf_nr = sum([1 for x in self.units if x['unit_type'] == 'E'])

    def combat_ended(self):
        types_left = set([x['unit_type'] for x in self.units if x['hp'] > 0])
        if len(types_left) == 1:
            return True
        return False

    def elf_killed(self):
        cur_elf_nr = sum(
            [1 for x in self.units if x['unit_type'] == 'E' and x['hp'] > 0])

        if cur_elf_nr == self.elf_nr:
            return False
        else:
            return True

    def simulate(self, stop_on_elf_death=False):
        round = 0
        while True:
            units_alive = [x for x in sorted(self.units, key=lambda k: [
                                             k['x'], k['y']]) if x['hp'] > 0]
            for unit in units_alive:
                if unit['hp'] <= 0:
                    continue
                if stop_on_elf_death and self.elf_killed():
                    print(f'Elf dead after {round} rounds')
                    return None

                if self.combat_ended():
                    hp_left = sum([x['hp']
                                   for x in self.units if x['hp'] > 0])

                    print(f'hp_left: {hp_left}')
                    print(f'Round: {round}')

                    print(f'res: {round * hp_left}')
                    return round * hp_left

                in_range = self.enemies_in_range(unit)

                if len(in_range) > 0:
                    # Attack
                    self.attack(unit, in_range)
                else:
                    self.move_unit(unit)
                    in_range = self.enemies_in_range(unit)

                    if len(in_range) > 0:
                        self.attack(unit, in_range)

            round += 1

    def move_unit(self, unit):
        # Find possible targets
        enemies = [u for u in self.units if unit['unit_type']
                   != u['unit_type'] and u['hp'] > 0]

        # find free space around targets
        in_range = []
        for enemy in enemies:
            tmp = list(self.cave_graph.neighbors(
                (enemy['x'], enemy['y'])))
            in_range += [
                x for x in tmp if self.cave_map[x[0]][x[1]] == '.']

        if len(in_range) == 0:
            # No ememy with free space
            return

        # Find all reachable spaces around targets
        reachable = []

        self.cave_graph.node[(unit['x'], unit['y'])]['free'] = True
        subgraph = self.cave_graph.subgraph([n for n, v in self.cave_graph.nodes(
            data=True) if v['free']])
        for pos in in_range:
            try:
                length = nx.shortest_path_length(
                    subgraph, (unit['x'], unit['y']), pos)

                reachable.append([pos, length])
            except nx.exception.NetworkXNoPath:
                pass
        self.cave_graph.node[(unit['x'], unit['y'])]['free'] = False

        if len(reachable) == 0:
            # No reachable spaces
            return

        # Chose the nearest one. If multiple first in reading order.
        min_dist = min([x[1] for x in reachable])
        nearest = [x[0] for x in reachable if x[1] == min_dist]
        chosen = sorted(nearest, key=lambda k: [k[0], k[1]])[0]

        neighbours = list(self.cave_graph.neighbors((unit['x'], unit['y'])))
        neighbours = [n for n in neighbours if self.cave_graph.node[n]['free']]
        if len(neighbours) == 0:
            return

        # Find the shortes path to the chosen space
        steps = []
        subgraph = self.cave_graph.subgraph([n for n, v in self.cave_graph.nodes(
            data=True) if v['free']])

        for neighbour in neighbours:
            try:
                length = nx.shortest_path_length(
                    subgraph, neighbour, chosen)
                steps.append([neighbour, length])

            except nx.exception.NetworkXNoPath:
                pass

        if len(steps) == 0:
            # No possible move
            return

        min_step = min([x[1] for x in steps])
        nearest = [x[0] for x in steps if x[1] == min_step]

        # Chosen (if multiple, first in reading order)
        chosen_step = sorted(nearest, key=lambda k: [k[0], k[1]])[0]

        # Move the unit
        self.cave_map[chosen_step[0]][chosen_step[1]] = unit['unit_type']
        self.cave_map[unit['x']][unit['y']] = '.'
        self.cave_graph.nodes[(unit['x'], unit['y'])]['free'] = True
        unit['x'] = chosen_step[0]
        unit['y'] = chosen_step[1]
        self.cave_graph.nodes[(unit['x'], unit['y'])]['free'] = False

        return

    def attack(self, unit, enemies_in_range):
        lowest_hp = min([x['hp'] for x in enemies_in_range])
        attack = [x for x in enemies_in_range if x['hp'] == lowest_hp]
        attack = sorted(attack, key=lambda k: [k['x'], k['y']])[0]

        attack['hp'] -= unit['ap']

        if attack['hp'] <= 0:
            # Dead..
            self.cave_map[attack['x']][attack['y']] = '.'
            self.cave_graph.nodes[(attack['x'], attack['y'])]['free'] = True

            attack['x'] = -1
            attack['y'] = -1

    def enemies_in_range(self, unit):
        unit_pos = (unit['x'], unit['y'])
        attack = []
        # Check neighbors in graph
        for possible_move in self.cave_graph.neighbors(unit_pos):
            for u in [x for x in self.units if x['hp'] > 0]:
                if unit['unit_type'] != u['unit_type']:
                    if u['x'] == possible_move[0] and u['y'] == possible_move[1]:
                        attack.append(u)
        return attack

    def create_board_graph(self, file):
        with open(file) as fp:
            self.cave_map = [list(x) for x in fp.read().split('\n') if x]

        self.units = []
        graph = nx.Graph()
        test = 0
        for x, l in enumerate(self.cave_map):
            for y, pos in enumerate(l):

                if pos != '#':
                    test += 1
                    posible_edges = [
                        (x+1, y),
                        (x-1, y),
                        (x, y+1),
                        (x, y-1)
                    ]

                    posible_edges = [
                        x for x in posible_edges if self.cave_map[x[0]][x[1]] != '#']

                    graph.add_edges_from([((x, y), p) for p in posible_edges])
                    graph.nodes[(x, y)]['free'] = True
                    # Save the units position
                    if pos == 'G' or pos == 'E':
                        if pos == 'E':
                            ap = self.elf_ap
                        else:
                            ap = 3

                        unit = {
                            'x': x,
                            'y': y,
                            'unit_type': pos,
                            'hp': 200,
                            'ap': ap,
                        }
                        self.units.append(unit)

                        graph.nodes[(x, y)]['free'] = False
        self.cave_graph = graph


def test_part1():
    assert NetElf('test0.txt').simulate() == 27730
    assert NetElf('test1.txt').simulate() == 36334
    assert NetElf('test2.txt').simulate() == 39514
    assert NetElf('test3.txt').simulate() == 27755
    assert NetElf('test4.txt').simulate() == 28944
    assert NetElf('test5.txt').simulate() == 18740


if __name__ == "__main__":
    a = NetElf('input.txt')
    print(f'Part1: {a.simulate()}')

    elf_ap = 4
    while True:
        a = NetElf('input.txt', elf_ap=elf_ap)
        ret = a.simulate(stop_on_elf_death=True)

        if ret != None:
            print(f'Part2: {ret}')
            break

        elf_ap += 1
