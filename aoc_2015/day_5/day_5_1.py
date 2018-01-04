# --- Day 5: Doesn't He Have Intern-Elves For This? ---
# part 1 - ok

with open('input.txt', 'r') as fp:
    words = [x.rstrip() for x in fp]

nice = []
bad = ['ab', 'cd', 'pq', 'xy']
vowels = [x for x in 'aeiou']
double_words = [chr(x)*2 for x in range(ord('a'), ord('z')+1)]

for word in words:
    if not any(x in word for x in bad) and \
            sum([1 if x in vowels else 0 for x in word]) >= 3 and \
            any(x in word for x in double_words):
        nice.append(word)

print(len(nice))
