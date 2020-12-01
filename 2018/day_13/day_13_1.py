# --- Day 13: Mine Cart Madness ---
# Part 1 - ok

with open('input.txt') as fp:
    tracks = [list(x) for x in fp.read().split('\n') if x]

turn = ['l', 's', 'r']
carts = []
# Find the possition of all the carts
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

while True:

    for cart in sorted(carts, key=lambda k: [k['x'], k['y']]):
        cur_x = cart['x']
        cur_y = cart['y']
        last_track = cart['on_track']
        direction = cart['direction']

        # Move cart and fix track behind
        if direction == '>':
            cart['x'] += 1
        elif direction == '<':
            cart['x'] -= 1
        elif direction == '^':
            cart['y'] -= 1
        elif direction == 'v':
            cart['y'] += 1
        
        tracks[cur_y][cur_x] = last_track
        cart['on_track'] = tracks[cart['y']][cart['x']]

        # Check if crached
        if len(set([f"{k['x']},{k['y']}" for k in carts])) < len(carts):
            print('CRASH!!')
            print(f"{cart['x']},{cart['y']}")
            exit(0)

        if cart['on_track'] == '+':
            action = turn[cart['turn']]
            cart['turn'] += 1
            if cart['turn'] == 3:
                cart['turn'] = 0
            # No need to change direction on 's'

            if action == 'l':
                if direction == '>':
                    cart['direction'] = '^'
                elif direction == '<':
                    cart['direction'] = 'v'
                elif direction == '^':
                    cart['direction'] = '<'
                elif direction == 'v':
                    cart['direction'] = '>'
            elif action == 'r':
                if direction == '>':
                    cart['direction'] = 'v'
                elif direction == '<':
                    cart['direction'] = '^'
                elif direction == '^':
                    cart['direction'] = '>'
                elif direction == 'v':
                    cart['direction'] = '<'

        elif cart['on_track'] == '-' or cart['on_track'] == '|':
            pass
        else:
            if cart['on_track'] == '/':
                if direction == '>':
                    cart['direction'] = '^'
                elif direction == '<':
                    cart['direction'] = 'v'
                elif direction == '^':
                    cart['direction'] = '>'
                elif direction == 'v':
                    cart['direction'] = '<'
            else:
                # on \
                if direction == '>':
                    cart['direction'] = 'v'
                elif direction == '<':
                    cart['direction'] = '^'
                elif direction == '^':
                    cart['direction'] = '<'
                elif direction == 'v':
                    cart['direction'] = '>'

        tracks[cart['y']][cart['x']] = cart['direction']
