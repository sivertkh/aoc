# --- Day 4: Repose Record ---
# Part 2 - ok

with open('input.txt') as fp:
    data = [x for x in fp.read().split('\n') if x]

on_duty = {}
sleep = {}

for line in data:
    tmp = line.split(' ')

    time = tmp[1].rstrip(']').split(':')

    d = tmp[0].lstrip('[')

    if tmp[2] == 'Guard':

        if time[0] != '00':

            date_tmp = d.split('-')

            month = int(date_tmp[1])
            day = int(date_tmp[2])

            if month == 2 and day == 28:
                d = f"{date_tmp[0]}-{'03'}-{'01'}"
            elif month == 3 and day == 31:
                d = f"{date_tmp[0]}-{'04'}-{'01'}"
            elif month == 4 and day == 30:
                d = f"{date_tmp[0]}-{'04'}-{'01'}"
            elif month == 5 and day == 31:
                d = f"{date_tmp[0]}-{'06'}-{'01'}"
            elif month == 6 and day == 30:
                d = f"{date_tmp[0]}-{'07'}-{'01'}"
            elif month == 7 and day == 31:
                d = f"{date_tmp[0]}-{'08'}-{'01'}"
            elif month == 8 and day == 31:
                d = f"{date_tmp[0]}-{'09'}-{'01'}"
            elif month == 9 and day == 30:
                d = f"{date_tmp[0]}-{'10'}-{'01'}"
            elif month == 10 and day == 31:
                d = f"{date_tmp[0]}-{'11'}-{'01'}"

            else:
                day = str(day+1).zfill(2)
                d = f"{date_tmp[0]}-{date_tmp[1]}-{day}"

        on_duty[d] = tmp[3]
        continue

    if time[0] != '00':
        continue

    if tmp[2] == 'falls' or tmp[2] == 'wakes':

        if d not in sleep:
            sleep[d] = ['.' for x in range(60)]

        if tmp[2] == 'falls':
            sleep[d][int(time[1])] = 'f'
        else:
            sleep[d][int(time[1])] = 'a'

updated = {}
for date, day in sleep.items():
    asleep = False
    updated[date] = ['.' for x in range(len(day))]
    for i in range(len(day)):
        if asleep:
            if day[i] == 'a':
                asleep = False
                updated[date][i] = '.'
            else:
                updated[date][i] = '#'
        else:
            if day[i] == 'f':
                asleep = True
                updated[date][i] = '#'

gard_sleep = {}
for date, m in updated.items():
    gard_id = on_duty[date]

    if gard_id not in gard_sleep:
        gard_sleep[gard_id] = []

    gard_sleep[gard_id].append(m)


res = {}
for k, v in gard_sleep.items():
    res[k] = [0 for i in range(60)]
    for day in v:
        for i in range(len(day)):
            if day[i] == '#':
                res[k][i] += 1


max_freq = 0
max_min = 0
max_id = None
for k, v in res.items():

    for i, v in enumerate(v):
        if v > max_freq:
            max_freq = v
            max_min = i
            max_id = k

print(int(max_id.lstrip('#')) * max_min)