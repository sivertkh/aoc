# --- Day 4: Repose Record ---
# Part 1 -

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

for date, day in updated.items():
    print(''.join(day))

asleep = {}
for date, day in updated.items():
    asleep[date] = len([x for x in day if x == '#'])


gard_sleep = {}
for date, m in asleep.items():
    gard_id = on_duty[date]

    if gard_id not in gard_sleep:
        gard_sleep[gard_id] = 0

    gard_sleep[gard_id] += m

max_sleep = 0
gid = None
for k, v in gard_sleep.items():
    print(f'{k} {v}')

    if v > max_sleep:
        max_sleep = v
        gid = k

print('--------------------')
print(f'{gid} {max_sleep}')

res = []
for date, m in updated.items():
    gard_id = on_duty[date]
    if gard_id != gid:
        continue
    res.append(m)

count = [0 for i in range(60)]

for r in res:

    for i in range(len(r)):
        if r[i] == '#':
            count[i] += 1

mx_c = 0
mx_i = 0
for i in range(60):
    if count[i] >= mx_c:
        mx_c = count[i]
        mx_i = i

print(f'{mx_c} {mx_i}')

print(int(gid.lstrip('#')) * mx_i)
