# --- Day 10: Syntax Scoring ---

with open("input.txt") as fp:
    lines = [[y for y in x.strip()] for x in fp.readlines()]

part_2_scores = []
part_1_score = 0
for line in lines:
    stack = []
    for character in line:
        if character in ['{', '(', '[', '<']:
            stack.append(character)
        else:
            if len(stack) > 0:
                last = stack.pop()
            else:
                last = None
            match character:
                case ')':
                    if last != '(':
                        part_1_score += 3
                        break
                case ']':
                    if last != '[':
                        part_1_score += 57
                        break
                case '}':
                    if last != '{':
                        part_1_score += 1197
                        break
                case '>':
                    if last != '<':
                        part_1_score += 25137
                        break
    else:
        score = 0
        for character in stack[::-1]:
            score = score * 5
            match character:
                case '(':
                    score += 1
                case '[':
                    score += 2
                case '{':
                    score += 3
                case '<':
                    score += 4
        part_2_scores.append(score)

print(f"Part 1: {part_1_score}")
part_2_score = sorted(part_2_scores)[len(part_2_scores)//2]
print(f"Part 2: {part_2_score}")
