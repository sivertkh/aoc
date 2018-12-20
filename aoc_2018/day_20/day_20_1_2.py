# --- Day 20: A Regular Map ---
# Part 1 -

from collections import deque


class Room(object):

    def __init__(self, nr):
        self.nr = nr
        self.next_rooms = []

    def __str__(self):
        return str(self.nr)


class Mapexer(object):

    def __init__(self):
        self.mapex = deque(list('^ENWWW(NEEE|SSE(EE|N))$'))
        #self.mapex = deque(list('^WNE$'))
        print(self.mapex)
        self.movments = ['N', 'S', 'E', 'W']

        self.start = Room(0)
        self.current = self.start
        self.rooms = []

    def find_path(self):

        while len(self.mapex) > 0:

            c = self.mapex.popleft()
            if c == '^':
                continue
            elif c == '$':
                print('At end!!')
                assert len(self.mapex) == 0
            elif c == '(':
                sub_string = [c]
                while c != ')':
                    # Pop from the stack until we have a valid subregex
                    c = self.mapex.popleft()
                    sub_string.append(c)

                print(sub_string)
            else:
                print(c)
                assert c in self.movments
                new_room = Room(self.current.nr+1)
                self.current.next_rooms.append(new_room)
                self.current = new_room
                self.rooms.append(new_room)
                # There should only be letters here

        for r in self.rooms:
            print(r)


if __name__ == "__main__":
    a = Mapexer()
    a.find_path()
