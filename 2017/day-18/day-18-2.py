# --- Day 18: Duet ---
# part 2 - ok

from queue import Queue, Empty
import threading


class aocThread(threading.Thread):

    def __init__(self, reg_init, inq, outq):
        threading.Thread.__init__(self)
        self.reg_init = reg_init
        self.inq = inq
        self.outq = outq

    def run(self):
        runner(self.reg_init, self.inq, self.outq)

def runner(register_init, inq, outq):

    position = 0
    register = {chr(c): register_init for c in range(ord('a'), ord('z'))}
    jumped = False
    send = 0
    while True:
        instruction = program[position]
        print("In thread {}, at {}".format(register_init, instruction))
        itype = instruction[0]

        try:
            x = int(instruction[1])
        except ValueError:
            x = register[instruction[1]]

        if len(instruction) == 3:
            try:
                y = int(instruction[2])
            except ValueError:
                y = register[instruction[2]]

        if itype == 'snd':
            # snd X
            send = send + 1
            outq.put(x)
        elif itype == 'set':
            # set X Y
            register[instruction[1]] = y
        elif itype == 'add':
            # add X Y
            register[instruction[1]] = x + y
        elif itype == 'mul':
            # mul X Y
            register[instruction[1]] = x * y
        elif itype == 'mod':
            # mod X Y
            register[instruction[1]] = x % y
        elif itype == 'rcv':
            # rcv X
            try:
                # The quick and dirty fix.. using timeout to find deadlock..
                register[instruction[1]] = inq.get(timeout=2)
            except Empty:
                print("Empty queue after 2 sec..")
                print("Thread {} send {} values".format(register_init, send))
                return
        elif itype == 'jgz':
            # jgz X Y
            if x > 0:
                # Do a jump to the left!
                position = position + y
                jumped = True

        if not jumped:
            position = position + 1
        else:
            jumped = False


if __name__ == '__main__':
    with open('input.txt', 'r') as fp:
        program = [x.split(" ") for x in fp.read().split('\n')]
    q1 = Queue()
    q2 = Queue()
    t1 = aocThread(0, q2, q1).start()
    t2 = aocThread(1, q1, q2).start()
