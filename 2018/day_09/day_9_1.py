# --- Day 9: Marble Mania ---
# Part 1 - ok

with open('input.txt') as fp:
    data = [x.split(' ') for x in fp.read().split('\n') if x]

nr_players = int(data[0][0])
last_marble = int(data[0][6])

circle = []
current_marble = 0
players = {i: 0 for i in range(nr_players)}
current_player = 1

for i in range(last_marble):
    if i == 0:
        circle.append(0)
        current_marble = 0
        continue

    if i % 23 == 0:
        players[current_player] += i
        current_marble -= 7
        if current_marble < 0:
            current_marble = len(circle) - 1 + current_marble

        players[current_player] += circle[current_marble]
        del circle[current_marble]

    else:
        current_marble += 2
        if current_marble >= len(circle):
            current_marble = len(circle) - current_marble
        circle.insert(current_marble, i)

    current_player += 1
    if current_player == len(players):
        current_player = 0

print(max(players.values()))
