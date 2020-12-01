# --- Day 4: The Ideal Stocking Stuffer ---
# part 1 - ok

from hashlib import md5

key = 'iwrupvqb'
i = 1
while True:
    k = "{}{}".format(key, i)
    a_hash = md5(k.encode('utf-8')).hexdigest()

    if a_hash[0] == '0':
        start = set(a_hash[:5])
        if len(start) == 1:
            print(i)
            exit(0)
    i += 1

