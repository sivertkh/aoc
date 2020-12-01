# --- Day 8: Space Image Format ---
# Part 1 - ok

width = 25
height = 6

with open('./input.txt') as fp:
    pic_input = [int(x) for x in fp.read().strip() if x]

layer_length = width * height

layers = [pic_input[i:i+layer_length]
          for i in range(0, len(pic_input), layer_length)]

zeros = [len([x for x in layer if x == 0]) for layer in layers]
min_index = zeros.index(min(zeros))

nr_1 = len([x for x in layers[min_index] if x == 1])
nr_2 = len([x for x in layers[min_index] if x == 2])

print(nr_1*nr_2)
