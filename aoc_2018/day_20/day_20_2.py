# --- Day 20: A Regular Map ---
# Part 2

from collections import deque

movments = ['E', 'S', 'W', 'N']
room_count = 0

class Room(object):

    def __init__(self, value):
        self.value = value
        self.rooms = []

    def add_room(self, room):

        if room is not None:
            self.rooms.append(room)

    def get_rooms(self):
        return self.rooms


def parse(subtree, subtree_distance):


    tmp = 0

    subtree_root = None
    current_room = None

    while len(subtree) > 0:
        c = subtree.popleft()

        if c == '^':
            continue
        elif c == '$':
            return 
        if c == '(':
            current_room.add_room(parse(subtree, subtree_distance+tmp))

        elif c == ')':
            return subtree_root 
        elif c == '|':
            tmp = 0


        elif c in movments:
            print(subtree_distance + tmp)
            if not subtree_root:
                current_room = Room(subtree_distance+tmp)
                subtree_root = current_room
            else:
                tmp += 1
                tmp_room = Room(subtree_distance+tmp)
                current_room.add_room(tmp_room)
                current_room = tmp_room

        else:
            print(f'??? {c}')


def find_lenght(root, current_pos):
    global room_count

    if current_pos > 1000:
        room_count += 1

    if len(root.get_rooms()) == 0:
        return

    for i in root.get_rooms:
        find_lenght(i, current_pos+1)



def main():

    with open('input.txt') as fp:
        mapex = deque(list(fp.read().rstrip('\n')))

    
    root = parse(mapex, 0)
    find_lenght(root, 0)

    print(room_count)


if __name__ == "__main__":

    main()

