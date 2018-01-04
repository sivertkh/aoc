# --- Day 5: Doesn't He Have Intern-Elves For This? ---
# part 2 -

with open('input.txt', 'r') as fp:
    words = [x.rstrip() for x in fp]

nice = []
bad = ['ab', 'cd', 'pq', 'xy']
vowels = [x for x in 'aeiou']
double_words = [chr(x)*2 for x in range(ord('a'), ord('z')+1)]

for word in words:
    pass
    # - It contains a pair of any two letters that appears at least twice in
    # the string without overlapping, like xyxy (xy) or aabcdefgaa (aa),
    # but not like aaa (aa, but it overlaps).

    #
    # i == i + 2
    # - It contains at least one letter which repeats with exactly one letter
    # between them, like xyx, abcdefeghi (efe), or even aaa.

print(len(nice))
