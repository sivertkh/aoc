# --- Day 16: Chronal Classification ---
# Part 2 - ok

with open('input.txt') as fp:
    data = [x for x in fp.read().split('\n\n\n')]
    part1_data = [x for x in data[0].split('\n') if x]
    part1_data = [part1_data[i:i + 3] for i in range(0, len(part1_data), 3)]
    part2_data = [[int(y) for y in x.split(' ')]
                  for x in data[1].split('\n') if x]

mapping = {}
for part in part1_data:
    registers_before = [int(x)
                        for x in part[0].split('[')[1].rstrip(']').split(',')]

    instruction = [int(x) for x in part[1].split(' ')]
    op_code = instruction[0]
    a = instruction[1]
    b = instruction[2]
    c = instruction[3]
    registers_after = [int(x)
                       for x in part[2].split('[')[1].rstrip(']').split(',')]

    res = {}
    addr_res = registers_before.copy()
    addr_res[c] = addr_res[a] + addr_res[b]
    res['addr'] = addr_res

    addi_res = registers_before.copy()
    addi_res[c] = addi_res[a] + b
    res['addi'] = addi_res

    mulr_res = registers_before.copy()
    mulr_res[c] = mulr_res[a] * mulr_res[b]
    res['mulr'] = mulr_res

    muli_res = registers_before.copy()
    muli_res[c] = muli_res[a] * b
    res['muli'] = muli_res

    banr_res = registers_before.copy()
    banr_res[c] = banr_res[a] & banr_res[b]
    res['banr'] = banr_res

    bani_res = registers_before.copy()
    bani_res[c] = bani_res[a] & b
    res['bani'] = bani_res

    borr_res = registers_before.copy()
    borr_res[c] = borr_res[a] | borr_res[b]
    res['borr'] = borr_res

    bori_res = registers_before.copy()
    bori_res[c] = bori_res[a] | b
    res['bori'] = bori_res

    setr_res = registers_before.copy()
    setr_res[c] = setr_res[a]
    res['setr'] = setr_res

    seti_res = registers_before.copy()
    seti_res[c] = a
    res['seti'] = seti_res

    gtir_res = registers_before.copy()
    if a > gtir_res[b]:
        gtir_res[c] = 1
    else:
        gtir_res[c] = 0
    res['gtir'] = gtir_res

    gtri_res = registers_before.copy()
    if gtri_res[a] > b:
        gtri_res[c] = 1
    else:
        gtri_res[c] = 0
    res['gtri'] = gtri_res

    gtrr_res = registers_before.copy()
    if gtrr_res[a] > gtrr_res[b]:
        gtrr_res[c] = 1
    else:
        gtrr_res[c] = 0
    res['gtrr'] = gtrr_res

    eqir_res = registers_before.copy()
    if a == eqir_res[b]:
        eqir_res[c] = 1
    else:
        eqir_res[c] = 0
    res['eqir'] = eqir_res

    eqri_res = registers_before.copy()
    if eqri_res[a] == b:
        eqri_res[c] = 1
    else:
        eqri_res[c] = 0
    res['eqri'] = eqri_res

    eqrr_res = registers_before.copy()
    if eqrr_res[a] == eqrr_res[b]:
        eqrr_res[c] = 1
    else:
        eqrr_res[c] = 0
    res['eqrr'] = eqrr_res

    correct = {k: v for k, v in res.items() if v == registers_after}
    for k, v in correct.items():
        if k not in mapping:
            mapping[k] = []
        mapping[k].append(op_code)

mapping = {k: list(set(v)) for k, v in mapping.items()}
final_mapping = {}
while True:
    one = {k: v for k, v in mapping.items() if len(v) == 1}
    for k, v in one.items():
        nr = v.pop()
        final_mapping[str(nr)] = k
        del mapping[k]

        for k, v in mapping.items():
            mapping[k] = [x for x in v if x != nr]

    if len(final_mapping) == 16:
        break

for k, v in final_mapping.items():
    print(f'{k}: {v}')

register = [0 for _ in range(4)]
for inst in part2_data:

    op_code = inst[0]
    a = inst[1]
    b = inst[2]
    c = inst[3]

    operation = final_mapping[str(op_code)]

    if operation == 'addr':
        register[c] = register[a] + register[b]
    elif operation == 'addi':
        register[c] = register[a] + b
    elif operation == 'mulr':
        register[c] = register[a] * register[b]
    elif operation == 'muli':
        register[c] = register[a] * b
    elif operation == 'banr':
        register[c] = register[a] & register[b]
    elif operation == 'bani':
        register[c] = register[a] & b
    elif operation == 'borr':
        register[c] = register[a] | register[b]
    elif operation == 'bori':
        register[c] = register[a] | b
    elif operation == 'setr':
        register[c] = register[a]
    elif operation == 'seti':
        register[c] = a
    elif operation == 'gtir':
        if a > register[b]:
            register[c] = 1
        else:
            register[c] = 0
    elif operation == 'gtri':
        if register[a] > b:
            register[c] = 1
        else:
            register[c] = 0
    elif operation == 'gtrr':
        if register[a] > register[b]:
            register[c] = 1
        else:
            register[c] = 0
    elif operation == 'eqir':
        if a == register[b]:
            register[c] = 1
        else:
            register[c] = 0
    elif operation == 'eqri':
        if register[a] == b:
            register[c] = 1
        else:
            register[c] = 0
    elif operation == 'eqrr':
        if register[a] == register[b]:
            register[c] = 1
        else:
            register[c] = 0

print(register[0])
