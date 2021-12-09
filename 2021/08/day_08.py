# --- Day 8: Seven Segment Search ---

with open("input.txt") as fp:
    numbers = [
        [
            list(map(lambda x: "".join(sorted(x)), y.split('|')[0].strip().split())),
            list(map(lambda x: "".join(sorted(x)), y.split('|')[1].strip().split()))
        ]
        for y in fp.readlines()
    ]

res_1 = res_2 = 0
for signal, output in numbers:

    res_1 += sum([1 for x in output if len(x) in [2, 3, 4, 7]])

    signal_mapping = {}
    signal_len = [len(x) for x in signal]

    for i, j in [(1, 2), (4, 4), (7, 3), (8, 7)]:
        signal_mapping[i] = signal[signal_len.index(j)]

    index_5 = [i for i, x in enumerate(signal_len) if x == 5]
    index_found_5 = []
    index_6 = [i for i, x in enumerate(signal_len) if x == 6]
    index_found_6 = []

    # find 3
    for x in index_5:
        if set(signal_mapping[1]).intersection(set(signal[x])) == set(signal_mapping[1]):
            signal_mapping[3] = signal[x]
            index_found_5.append(x)
            break

    # find 9
    for x in index_6:
        if set(signal_mapping[3]).intersection(set(signal[x])) == set(signal_mapping[3]):
            signal_mapping[9] = signal[x]
            index_found_6.append(x)
            break

    # find 5 (and 2)
    for x in list(set(index_5) - set(index_found_5)):
        if len(list(set(signal_mapping[9]) - set(signal[x]))) == 1:
            signal_mapping[5] = signal[x]
            index_found_5.append(x)
            signal_mapping[2] = signal[list(set(index_5) - set(index_found_5))[0]]
            break

    # Find 0 (and 6)
    for x in list(set(index_6) - set(index_found_6)):
        if set(signal_mapping[1]).intersection(set(signal[x])) == set(signal_mapping[1]):
            signal_mapping[0] = signal[x]
            index_found_6.append(x)
            signal_mapping[6] = signal[list(set(index_6) - set(index_found_6))[0]]
            break

    # Flip mapping
    signal_mapping = {v: k for k,v in signal_mapping.items()}
    res_2 += int("".join([str(signal_mapping[x]) for x in output]))

print(f"Part 1: {res_1}")
print(f"Part 2: {res_2}")
