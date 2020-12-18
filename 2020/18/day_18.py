# --- Day 18: Operation Order ---
from collections import deque
from tokenize import tokenize, NUMBER, OP, NEWLINE


def token_runner(tokens):
    cur_operator = None
    cur_sum = 0
    values = []
    while tokens:
        token = tokens.popleft()
        if token.type == NUMBER:
            if cur_sum:
                cur_sum = str(eval("".join([cur_sum, cur_operator, token.string])))
                cur_operator = None
            else:
                cur_sum = token.string
        elif token.type == OP:
            if token.string == "(":
                if cur_sum:
                    cur_sum = str(
                        eval("".join([cur_sum, cur_operator, token_runner(tokens)]))
                    )
                else:
                    cur_sum = token_runner(tokens)
            elif token.string == ")":
                return cur_sum
            cur_operator = token.string
        elif token.type == NEWLINE:
            values.append(int(cur_sum))
            cur_sum = 0
            cur_operator = None
    return values


def token_runner2(tokens):
    cur_operator = None
    cur_num = None
    cur_str = []
    values = []
    while tokens:
        token = tokens.popleft()
        if token.type == NUMBER:
            if cur_num:
                if cur_operator == "+":
                    cur_num = str(eval("".join([cur_num, cur_operator, token.string])))
                    cur_operator = None
                else:
                    cur_str.append(cur_num)
                    cur_str.append(cur_operator)
                    cur_num = token.string
                    cur_operator = None
            else:
                cur_num = token.string
        elif token.type == OP:
            if token.string == "(":
                if cur_operator:
                    inner_value = token_runner2(tokens)
                    if cur_operator == "+":
                        cur_num = str(
                            eval("".join([cur_num, cur_operator, inner_value]))
                        )
                        cur_operator = None
                    else:
                        cur_str.append(cur_num)
                        cur_str.append(cur_operator)
                        cur_num = inner_value
                        cur_operator = None
                else:
                    cur_num = token_runner2(tokens)
            elif token.string == ")":
                if cur_num:
                    cur_str.append(cur_num)
                return str(eval("".join(cur_str)))
            else:
                cur_operator = token.string
        elif token.type == NEWLINE:
            if cur_num:
                cur_str.append(cur_num)
            values.append(eval("".join(cur_str)))
            cur_str = []
            cur_operator = None
            cur_num = None
    return values


with open("input.txt", "rb") as f:
    tokens = deque([t for t in tokenize(f.readline)])

print(f"Part 1: {sum(token_runner(tokens.copy()))}")
print(f"Part 2: {sum(token_runner2(tokens))}")
