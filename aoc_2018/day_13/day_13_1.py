# --- Day 13: Mine Cart Madness ---
# Part 1 -


with open('simple.txt') as fp:
    tracks = [list(x) for x in fp.read().split('\n') if x]


for t in tracks:
    print(list(t))


# Fin the possition of all trains

turn = ['l', 's', 'r']
carts = []

for y, track in enumerate(tracks):
    for x, pos in enumerate(track):
        # We assume that the carts always start on a straight track..
        if pos == '>' or pos == '<':
            carts.append({
                'x': x,
                'y': y,
                'direction': pos,
                'turn': 0,
                'on_track': '-',
            })

        elif pos == '^' or pos == 'v':
            carts.append({
                'x': x,
                'y': y,
                'direction': pos,
                'turn': 0,
                'on_track': '|',
            })

print(carts)

# For each turn
# sort carts by position on map
# move carts in order
# for each move check if crash
# update cart position
#

while True:

    new_carts = []
    for cart in sorted(carts, key=lambda k: [k['x'], k['y']]):

        cur_x = cart['x']
        cur_y = cart['y']
        last_track = cart['on_track']
        direction = cart['direction']

        if cart['on_track'] == '+':

            action = turn[cart['turn']]
            cart['turn'] += 1
            if cart['turn'] == 3:
                cart['turn'] == 0

            if action == 's':
                if direction == '>':
                    cart['x'] += 1
                elif direction == '<':
                    cart['x'] -= 1
                elif direction == '^':
                    cart['y'] -= 1
                elif direction == 'v':
                    cart['y'] += 1

            elif action == 'l':

                if direction == '>':
                    cart['direction'] = '^'
                    cart['y'] -= 1
                elif direction == '<':
                    cart['direction'] = 'v'
                    cart['y'] += 1
                elif direction == '^':
                    cart['direction'] = '<'
                    cart['x'] -= 1
                elif direction == 'v':
                    cart['direction'] = '>'
                    cart['x'] += 1

            elif action == 'r':
                if direction == '>':
                    cart['direction'] = 'v'
                    cart['y'] += 1
                elif direction == '<':
                    cart['direction'] = '^'
                    cart['y'] -= 1
                elif direction == '^':
                    cart['direction'] = '>'
                    cart['x'] += 1
                elif direction == 'v':
                    cart['direction'] = '<'
                    cart['x'] -= 1

        elif cart['on_track'] == '-' or cart['on_track'] == '|':
            if direction == '>':
                cart['x'] += 1
            elif direction == '<':
                cart['x'] -= 1
            elif direction == '^':
                cart['y'] -= 1
            elif direction == 'v':
                cart['y'] += 1

        else:
            if cart['on_track'] == '/':
                if direction == '>':
                    cart['direction'] = '^'
                    cart['y'] -= 1
                elif direction == '<':
                    cart['direction'] = 'v'
                    cart['y'] += 1
                elif direction == '^':
                    cart['direction'] = '>'
                    cart['x'] += 1
                elif direction == 'v':
                    cart['direction'] = '<'
                    cart['x'] -= 1
            else:
                # on \
                if direction == '>':
                    cart['direction'] = 'v'
                    cart['y'] += 1
                elif direction == '<':
                    cart['direction'] = '^'
                    cart['y'] -= 1
                elif direction == '^':
                    cart['direction'] = '<'
                    cart['x'] -= 1
                elif direction == 'v':
                    cart['direction'] = '>'
                    cart['x'] += 1

        # Move cart and fix track behind
        tracks[cur_y][cur_x] = last_track

        # TODO do we need to update the track?
        cart['on_track'] = track[cart['x']][cart['y']]
        track[cart['x']][cart['y']] = cart['direction']

        # Chec if crached
        if len(set([[k['x'], k['y']] for k in carts])) < len(carts):
            print('CRASH!!')
            print(carts)
            exit(0)
