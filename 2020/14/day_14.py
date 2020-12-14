# --- Day 14: Docking Data ---
import re

with open('input.txt') as fp:
    insts = [x.rstrip('\n').split(' = ') for x in fp.readlines()]

memory = {}
mask_0 = 0
mask_1 = 0
for inst in insts:
    if inst[0] == 'mask':
        mask_0 = int(''.join(['0' if x == '0' else '1' for x in inst[1]]), 2)
        mask_1 = int(''.join(['1' if x == '1' else '0' for x in inst[1]]), 2)
    else:
        nr = int(inst[1])
        flipped = (nr | mask_1) & mask_0
        memory[inst[0]] = flipped

print(f'Part1: {sum(memory.values())}')


def create_addrs(addr):
    for i, x in enumerate(addr):
        if x == 'X':
            addr_a = addr.copy()
            addr_b = addr.copy()
            addr_a[i] = '0'
            addr_b[i] = '1'
            ret_a = create_addrs(addr_a)
            ret_b = create_addrs(addr_b)
            ret = []
            ret.extend(ret_a)
            ret.extend(ret_b)
            return ret
    return [addr]


memory_2 = {}
mask_1 = 0
mask = []
for inst in insts:
    if inst[0] == 'mask':
        mask_1 = int(''.join(['1' if x == '1' else '0' for x in inst[1]]), 2)
        mask = [x for x in inst[1]]
    else:
        nr = int(inst[1])
        addr = int(re.search(r'mem\[(\d*)\]', inst[0]).group(1))

        flipped = addr | mask_1
        flipped = [x for x in bin(flipped)[2:]]
        padded = ['0' for x in range(len(mask)-len(flipped))]
        padded.extend(flipped)
        for i in range(len(padded)):
            if mask[i] == 'X':
                padded[i] = 'X'
        addrs = create_addrs(padded)
        addrs = set([int("".join(x), 2) for x in addrs])
        for addr in addrs:
            memory_2[addr] = nr

print(f'Part2: {sum(memory_2.values())}')
