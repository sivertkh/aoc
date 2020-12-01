# --- Day 16: Chronal Classification ---
# Part 1 - ok

with open('input.txt') as fp:

    data = [x for x in fp.read().split('\n\n\n')]
    part1_data = [x for x in data[0].split('\n') if x]
    part1_data = [part1_data[i:i + 3] for i in range(0, len(part1_data), 3)]

three_or_more = 0
for part in part1_data:
    registers_before = [int(x)
                        for x in part[0].split('[')[1].rstrip(']').split(',')]

    instruction = [int(x) for x in part[1].split(' ')]
    op_code = instruction[0]
    a = instruction[1]
    b = instruction[2]
    c = instruction[3]

    res = []
    registers_after = [int(x)
                       for x in part[2].split('[')[1].rstrip(']').split(',')]

    addr_res = registers_before.copy()
    addr_res[c] = addr_res[a] + addr_res[b]
    res.append(addr_res)

    addi_res = registers_before.copy()
    addi_res[c] = addi_res[a] + b
    res.append(addi_res)

    mulr_res = registers_before.copy()
    mulr_res[c] = mulr_res[a] * mulr_res[b]
    res.append(mulr_res)

    muli_res = registers_before.copy()
    muli_res[c] = muli_res[a] * b
    res.append(muli_res)

    banr_res = registers_before.copy()
    banr_res[c] = banr_res[a] & banr_res[b]
    res.append(banr_res)

    bani_res = registers_before.copy()
    bani_res[c] = bani_res[a] & b
    res.append(bani_res)

    borr_res = registers_before.copy()
    borr_res[c] = borr_res[a] | borr_res[b]
    res.append(borr_res)

    bori_res = registers_before.copy()
    bori_res[c] = bori_res[a] | b
    res.append(bori_res)

    setr_res = registers_before.copy()
    setr_res[c] = setr_res[a]
    res.append(setr_res)

    seti_res = registers_before.copy()
    seti_res[c] = a
    res.append(seti_res)

    gtir_res = registers_before.copy()
    if a > gtir_res[b]:
        gtir_res[c] = 1
    else:
        gtir_res[c] = 0
    res.append(gtir_res)

    gtri_res = registers_before.copy()
    if gtri_res[a] > b:
        gtri_res[c] = 1
    else:
        gtri_res[c] = 0
    res.append(gtri_res)

    gtrr_res = registers_before.copy()
    if gtrr_res[a] > gtrr_res[b]:
        gtrr_res[c] = 1
    else:
        gtrr_res[c] = 0
    res.append(gtrr_res)

    eqir_res = registers_before.copy()

    if a == eqir_res[b]:
        eqir_res[c] = 1
    else:
        eqir_res[c] = 0
    res.append(eqir_res)

    eqri_res = registers_before.copy()

    if eqri_res[a] == b:
        eqri_res[c] = 1
    else:
        eqri_res[c] = 0
    res.append(eqri_res)

    eqrr_res = registers_before.copy()

    if eqrr_res[a] == eqrr_res[b]:
        eqrr_res[c] = 1
    else:
        eqrr_res[c] = 0
    res.append(eqrr_res)

    if len([x for x in res if x == registers_after]) >= 3:
        three_or_more += 1

print(three_or_more)
