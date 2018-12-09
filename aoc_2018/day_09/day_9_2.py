# --- Day 9: Marble Mania ---
# Part 2 - ok


with open('input.txt') as fp:
    data = [x.split(' ') for x in fp.read().split('\n') if x]

nr_players = int(data[0][0])
last_marble = int(data[0][6])*100

current_marble = None
players = {i: 0 for i in range(nr_players)}
current_player = 1
start = None

for i in range(last_marble):
    if i == 0:
        tmp = {}
        tmp['before'] = tmp
        tmp['next'] = tmp
        tmp['value'] = 0
        current_marble = tmp
        start = tmp
        continue

    if i % 23 == 0:
        players[current_player] += i
        for _ in range(7):
            current_marble = current_marble['before']

        players[current_player] += current_marble['value']
        current_marble['before']['next'] = current_marble['next']
        current_marble['next']['before'] = current_marble['before']
        current_marble = current_marble['next']

    else:
        for _ in range(2):
            current_marble = current_marble['next']
        element = {
            'before': current_marble['before'],
            'next': current_marble,
            'value': i
        }
        current_marble['before']['next'] = element
        current_marble['before'] = element
        current_marble = element

    current_player += 1
    if current_player == len(players):
        current_player = 0

print(max(players.values()))
