# --- Day 20: A Regular Map ---
# Part 1 -

from collections import deque


class Mapexer(object):

    def __init__(self):
        #self.mapex = deque(list('^ENWWW(NEEE|SSE(EE|N))$'))
        self.mapex = deque(list('^WNE$'))
        print(self.mapex)
        self.movments = ['N', 'S', 'E', 'W']

        self.size = len([x for x in self.mapex if x in self.movments])
        print(self.size)
        self.size = 10
        self.area = [[' ' for x in range(self.size)] for y in range(self.size)]

        # Start position
        self.pos_x = self.size // 2
        self.pos_y = self.size // 2

    def add_walls(self):

        for x in range(self.size):
            for y in range(self.size):
                if self.area[x][y] == ' ' or self.area[x][y] == '?':
                    self.area[x][y] = '#'

    def add_unknown(self, x, y):
        neighbours = [
            [x+1, y],
            [x-1, y],
            [x, y+1],
            [x, y-1]
        ]
        # Fill inn unknown
        for n in neighbours:
            if self.area[n[0]][n[1]] == ' ':
                self.area[n[0]][n[1]] = '?'

    def move(self, direction):
        assert direction in self.movments

        start_x = self.pos_x
        start_y = self.pos_y

        if direction == 'N':
            self.area[self.pos_x-1][self.pos_y] = '-'
            self.add_unknown(self.pos_x-1, self.pos_y)
            self.pos_x -= 2
        elif direction == 'S':
            self.area[self.pos_x+1][self.pos_y] = '-'
            self.add_unknown(self.pos_x+1, self.pos_y)
            self.pos_x += 2
        elif direction == 'E':
            self.area[self.pos_x][self.pos_y+1] = '|'
            self.add_unknown(self.pos_x, self.pos_y+1)
            self.pos_y += 2
        else:
            self.area[self.pos_x][self.pos_y-1] = '|'
            self.add_unknown(self.pos_x, self.pos_y-1)
            self.pos_y -= 2

        self.area[start_x][start_y] = '.'
        self.area[self.pos_x][self.pos_y] = 'X'

        self.add_unknown(self.pos_x, self.pos_y)

    def print_map(self):
        while len(self.mapex) > 0:

            c = self.mapex.popleft()
            if c == '^':
                continue
            elif c == '$':
                print('At end!!')
                assert len(self.mapex) == 0
            elif c == '(':
                while True:
                    # Pop from the stack until we have a valid subregex
                    c = self.mapex.pop()
            else:
                print(c)
                self.move(c)
                # There should only be letters here
                assert c in self.movments

        self.add_walls()
        for i in self.area:
            print(''.join(i))


if __name__ == "__main__":
    a = Mapexer()
    a.print_map()
