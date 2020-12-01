# --- Day 9: Stream Processing ---
# part 1 - ok

with open('input.txt', 'r') as fp:
    stream = fp.read().rstrip()

# Removing the ! parts
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

# Removing garbage
in_garbage = None
fixed2 = []
for i in fixed:

    if in_garbage:
        if i == '>':
            # End of garbage!
            in_garbage = False
    else:
        if i == '<':
            # Start of garbage!
            in_garbage = True
        else:
            fixed2.append(i)

level = 0
s = 0

# Counting the groups
for i in fixed2:
    if i == '{':
        # Opening a new
        level = level + 1
    elif i == '}':
        # Closing
        s = s + level
        level = level - 1

print(s)
