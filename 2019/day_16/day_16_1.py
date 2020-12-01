# --- Day 16: Flawed Frequency Transmission ---
# Part 1 - ok

import math
import numpy as np

with open('./input.txt') as fp:
    input_signal = [list(x) for x in fp.read().split('\n') if x][0]
    input_signal = np.array([np.array([int(x) for x in input_signal]) for _
                                      in range(len(input_signal))])

nr_phases = 100
base_pattern = [0, 1, 0, -1]

patterns = np.zeros((len(input_signal), len(input_signal)))
for i in range(1, len(input_signal)+1):
    pattern = [x for x in base_pattern for _ in range(i)]
    if len(input_signal) + 1 > len(pattern):
        mul = math.ceil((len(input_signal)+10)/len(pattern))
        pattern = np.array([x for _ in range(mul) for x in pattern])
    patterns[i-1] = pattern[1:len(input_signal)+1]

signal = input_signal
for phase in range(1, nr_phases+1):
    res = np.multiply(signal, patterns)
    new_signal = [int(str(int(x))[-1]) for x in np.sum(res, axis=1)]
    signal = np.array([np.array([int(x) for x in new_signal]) for _ in range(
        len(new_signal))])

print(''.join([str(x) for x in signal[0][:8]]))
