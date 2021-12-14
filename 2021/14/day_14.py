# --- Day 14: Extended Polymerization ---

from collections import Counter, defaultdict

def calc_answer(bigram_count, start, end):
    char_count = defaultdict(int)
    for k, v in bigrams_count.items():
        char_count[k[0]] += v
        char_count[k[1]] += v

    # Add the start and end
    char_count[start] += 1
    char_count[end] += 1
    max_count = max(char_count.values())
    min_count = min(char_count.values())
    return max_count//2 - min_count//2


with open("input.txt") as fp:
    template, rules = fp.read().strip().split("\n\n")
    template = template.strip()
    rules = {x.split(' -> ')[0]: x.split(' -> ')[1]  for x in rules.split('\n')}

start = template[0]
end = template[-1]

bigrams_count = defaultdict(int)
for value, count in Counter([template[i]+template[i+1] for i in range(len(template)-1)]).most_common():
    bigrams_count[value] = count

for i in range(40):
    new_bigrams = defaultdict(int)
    for bigram, count in bigrams_count.items():
        tmp = bigram[0] + rules[bigram]
        tmp2 = rules[bigram] + bigram[1]
        new_bigrams[tmp] += count
        new_bigrams[tmp2] += count
        new_bigrams[bigram] -= count

    for k, v in new_bigrams.items():
        bigrams_count[k] += v

    if i == 9:
        print(f"Part 1: {calc_answer(bigrams_count, start, end)}")

print(f"Part 2: {calc_answer(bigrams_count, start, end)}")
