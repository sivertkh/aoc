# --- Day 8: Matchsticks ---

import math

def solve(nr, start, end=None, sub_packets=None):
    cur_pos = start
    cur_numbers = []
    nr_packets = 1
    version_sum = 0

    while True:
        if cur_pos > len(nr):
            break
        if end and cur_pos+6 > end:
            break
        if sub_packets and nr_packets == sub_packets +1:
            break

        nr_packets += 1
        version_sum += int(nr[cur_pos:cur_pos+3], 2)
        type_id = int(nr[cur_pos+3:cur_pos+6], 2)
        cur_pos += 6
        if type_id == 4:
            value = ""
            while True:
                bits = nr[cur_pos:cur_pos+5]
                gr = bits[0]
                value += bits[1:]
                cur_pos += 5
                if gr == '0':
                    break
            cur_numbers.append(int(value, 2))

        else:
            length_type_id = nr[cur_pos]
            cur_pos += 1

            sub_bit_length = None
            sub_length = None

            if length_type_id == '0':
                sub_bit_length = int(nr[cur_pos:cur_pos+15], 2)
                cur_pos += 15

            elif length_type_id == '1':
                sub_length = int(nr[cur_pos:cur_pos+11], 2)
                cur_pos += 11

            new_end = cur_pos+sub_bit_length if sub_bit_length else None
            sub_values, new_position, sub_version_sum = solve(nr, cur_pos, new_end, sub_length)
            version_sum += sub_version_sum
            cur_pos = new_position

            match type_id:
                case 0:
                    cur_numbers.append(sum(sub_values))
                case 1:
                    cur_numbers.append(math.prod(sub_values))
                case 2:
                    cur_numbers.append(min(sub_values))
                case 3:
                    cur_numbers.append(max(sub_values))
                case 5:
                    cur_numbers.append(int(sub_values[0] > sub_values[1]))
                case 6:
                    cur_numbers.append(int(sub_values[0] < sub_values[1]))
                case 7:
                    cur_numbers.append(int(sub_values[0] == sub_values[1]))

    return cur_numbers, cur_pos, version_sum


with open('input.txt') as fp:
    nr = "".join([str(bin(int(x, 16)))[2:].zfill(4) for x in fp.readline().strip()])
    
res_2, _, res_1 = solve(nr, 0, len(nr))
print(f"Part 1: {res_1}")
print(f"Part 2: {res_2[0]}")
