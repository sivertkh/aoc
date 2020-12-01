# --- Day 9: Stream Processing ---
# part 2 - ok

with open('input.txt', 'r') as fp:
    stream = fp.read().rstrip()

# Remove the ! part
last = None
fixed = []
for i in stream:
    if last is None:
        # First or skipped
        if i != '!':
            fixed.append(i)
        last = i
    else:

        if last == '!':
            # Skipping current!
            last = None
        else:
            if i != '!':
                fixed.append(i)
            last = i

# Remove and count the garbage
in_garbage = None
garbage = 0
for i in fixed:
    if in_garbage:
        if i == '>':
            # End of garbage!
            in_garbage = False
        else:
            garbage = garbage + 1
    else:
        if i == '<':
            # Start of garbage!
            in_garbage = True

print(garbage)
