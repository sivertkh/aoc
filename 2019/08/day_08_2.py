# --- Day 8: Space Image Format ---
# Part 2 - ok

width = 25
height = 6

with open('./input.txt') as fp:
    pic_input = [int(x) for x in fp.read().strip() if x]

layer_length = width * height

layers = [pic_input[i:i+layer_length]
          for i in range(0, len(pic_input), layer_length)]

layers = [[x[i:i+width]
           for i in range(0, layer_length, width)] for x in layers]

rendered_image = [[-1 for _ in range(width)] for _ in range(height)]

for layer in layers:
    for i in range(len(layer)):
        for j in range(len(layer[i])):
            if rendered_image[i][j] == -1 and layer[i][j] != 2:
                rendered_image[i][j] = layer[i][j]

for i in rendered_image:
    print(''.join([' ' if x == 0 else '#' for x in i]))
