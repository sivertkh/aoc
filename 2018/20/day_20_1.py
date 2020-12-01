# --- Day 20: A Regular Map ---
# Part 1 - ok

from collections import deque

movments = ['E', 'S', 'W', 'N']

def parse(stack):
    results = []
    tmp = 0
    while len(stack) > 0:
        c = stack.popleft()
        if c == '^':
            continue
        elif c == '$':
            results.append(tmp)
            return max(results)
        if c == '(':
            tmp += parse(stack)
        elif c == ')':

            if tmp == 0:
                # This could give the wrong result if there is a 
                # large loop.
                return 0

            results.append(tmp)
            return max(results)
        elif c == '|':
            results.append(tmp)
            tmp = 0
        elif c in movments:
            tmp += 1
        else:
            print(f'??? {c}')


def main():

    with open('input.txt') as fp:
        mapex = deque(list(fp.read().rstrip('\n')))

    print(parse(mapex))
    

if __name__ == "__main__":

    main()

