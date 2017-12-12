

with open('./input.txt', 'r') as fp:
    data = map(int, fp.read().rstrip())


# Rotating so that we can igore the circular aspect of the problem.
# This will not work if the data consists on only one or thow types of numbers
# 1111111, 122222 ect
while True:
    print data
    if data[-1] == data[0]:
        tmp = data[1:] + data[:1]
        data = tmp
    else:
        break

last = -1
cur = -1
nr = 0
s = 0

for i in data:

    # skip the fist iteration
    if last != -1:
        if i == last:
            nr = nr + 1
        else:
            if nr != 0:
                # Saveing a sum
                tmp = last * (nr)
                print("Found {0} {1}, sum = {2}".format(nr, last, tmp))
                
                s = s + tmp

                # reset
                nr = 0

    last = i

if nr != 0:
    print("Found {0} {1}".format(nr, last))
    s = s + (last * (nr))

print("Sum: {}".format(s))
