import sys
import itertools
from queue import SimpleQueue
# --- Day 13: Care Package ---
# Part 2 -


class IntcodeRunner(object):
    def __init__(self, program, break_on_output=False):
        self.ip = 0
        self.relative_base = 0
        self.program = program + [0 for _ in range(1000)]
        self.input_buffer = SimpleQueue()
        self.output_buffer = SimpleQueue()
        self._halted = False
        self._waiting = False
        self.break_on_output = break_on_output

    def add_input(self, input):
        self.input_buffer.put(input)

    def get_output(self):
        if self.output_buffer.empty():
            return None
        return self.output_buffer.get()

    def program_has_output(self):
        return self.output_buffer.empty()

    def halted(self):
        return self._halted

    def waiting(self):
        return self._waiting

    def run_program(self):
        if self._halted:
            return
        while True:
            inst = [int(x) for x in str(self.program[self.ip])]
            if len(inst) == 1:
                opcode = inst[0]
                mode = []
            else:
                opcode = int(''.join([str(x) for x in inst[-2:]]))
                mode = inst[:-2]
                mode.reverse()

            if opcode == 1:
                self._add(mode)
            elif opcode == 2:
                self._mul(mode)
            elif opcode == 3:
                print("INPUT!")
                if not self._input(mode):
                    print('Breaking for input')
                    break
            elif opcode == 4:
                self._output(mode)
                if self.break_on_output:
                    break
            elif opcode == 5:
                self._jmp_true(mode)
            elif opcode == 6:
                self._jmp_false(mode)
            elif opcode == 7:
                self._lt(mode)
            elif opcode == 8:
                self._eq(mode)
            elif opcode == 9:
                self._adjust_rb(mode)
            elif opcode == 99:
                self._halted = True
                print('Halting!')
                break
            else:
                print(f'Unknown opcode.. {opcode}')
                sys.exit(1)

    def adjust_mode(self, mode_array, nr_param):
        if len(mode_array) == nr_param:
            return mode_array
        missing = [0 for _ in range(nr_param - len(mode_array))]
        return mode_array + missing

    def get_mode_value(self, mode, ip_offset):
        if mode == 0:
            pass
            return self.program[self.program[self.ip + ip_offset]]
        elif mode == 1:
            return self.program[self.ip + ip_offset]
        elif mode == 2:
            return self.program[self.program[self.ip + ip_offset] + self.relative_base]
        else:
            print(f'Got illigal mode! mode: {mode}')
            sys.exit(1)

    def expand_memory(self, nr):
        self.program = self.program + [0 for _ in range(nr*2)]

    def write_mode_value(self, mode, ip_offset, value):
        if mode == 0:
            if self.program[self.ip + ip_offset] >= len(self.program):
                self.expand_memory(self.program[self.ip + ip_offset])

            self.program[self.program[self.ip + ip_offset]] = value
        elif mode == 1:
            print('Wrong write mode!')
            sys.exit(1)
        elif mode == 2:
            if (self.program[self.relative_base + self.program[self.ip + ip_offset]] > len(self.program)):
                self.expand_memory(self.program[self.ip + ip_offset])

            self.program[self.relative_base +
                         self.program[self.ip + ip_offset]] = value
        else:
            print('Unknown write mode!')
            sys.exit(1)

    def _add(self, mode):
        mode = self.adjust_mode(mode, 3)
        param_1 = self.get_mode_value(mode[0], 1)
        param_2 = self.get_mode_value(mode[1], 2)
        self.write_mode_value(mode[2], 3, param_1 + param_2)
        self.ip += 4

    def _mul(self, mode):
        mode = self.adjust_mode(mode, 3)
        param_1 = self.get_mode_value(mode[0], 1)
        param_2 = self.get_mode_value(mode[1], 2)
        self.write_mode_value(mode[2], 3, param_1 * param_2)
        self.ip += 4

    def _input(self, mode):
        # Throws a queue.empty() if empty. We use this to input values
        mode = self.adjust_mode(mode, 1)
        if self.input_buffer.empty():
            self._waiting = True
            return False
        self.write_mode_value(mode[0], 1, self.input_buffer.get_nowait())
        self.ip += 2
        self._waiting = False
        return True

    def _output(self, mode):
        mode = self.adjust_mode(mode, 1)
        output = self.get_mode_value(mode[0], 1)
        self.output_buffer.put(output)
        self.ip += 2

    def _jmp_true(self, mode):
        # Jump if true
        mode = self.adjust_mode(mode, 2)
        jmp = self.get_mode_value(mode[0], 1)
        if jmp > 0:
            self.ip = self.get_mode_value(mode[1], 2)
        else:
            self.ip += 3

    def _jmp_false(self, mode):
        # Jump if false
        mode = self.adjust_mode(mode, 2)
        jmp = self.get_mode_value(mode[0], 1)
        if jmp == 0:
            self.ip = self.get_mode_value(mode[1], 2)
        else:
            self.ip += 3

    def _lt(self, mode):
        # less then
        mode = self.adjust_mode(mode, 3)
        param_1 = self.get_mode_value(mode[0], 1)
        param_2 = self.get_mode_value(mode[1], 2)

        if param_1 < param_2:
            self.write_mode_value(mode[2], 3, 1)
        else:
            self.write_mode_value(mode[2], 3, 0)
        self.ip += 4

    def _eq(self, mode):
        # equals
        mode = self.adjust_mode(mode, 3)
        param_1 = self.get_mode_value(mode[0], 1)
        param_2 = self.get_mode_value(mode[1], 2)

        if param_1 == param_2:
            self.write_mode_value(mode[2], 3, 1)
        else:
            self.write_mode_value(mode[2], 3, 0)
        self.ip += 4

    def _adjust_rb(self, mode):
        """Update the relative base."""
        mode = self.adjust_mode(mode, 1)
        self.relative_base += self.get_mode_value(mode[0], 1)
        self.ip += 2
        #print(f'RB updated, new value: {self.relative_base}')


def draw(screen):
    for x in screen:
        print(''.join(x))


with open('./input.txt') as fp:
    program_orign = [int(x) for x in fp.read().split(',') if x]

program_orign[0] = 2
program = IntcodeRunner(program_orign.copy())


# 0 is an empty tile. No game object appears in this tile.
# 1 is a wall tile. Walls are indestructible barriers.
# 2 is a block tile. Blocks can be broken by the ball.
# 3 is a horizontal paddle tile. The paddle is indestructible.
# 4 is a ball tile. The ball moves diagonally and bounces off objects.

size_x = 43
size_y = 26
screen = [[' ' for _ in range(size_x)] for _ in range(size_y)]
score = 0

program.run_program()
while not program.halted() or program.program_has_output():

    x_pos = program.get_output()
    y_pos = program.get_output()

    if x_pos == -1 and y_pos == 0:
        score = program.get_output()
        print(score)
    elif x_pos != None and y_pos != None:
        tile_type = program.get_output()
        if tile_type == 0:
            screen[y_pos][x_pos] = ' '
        elif tile_type == 1:
            screen[y_pos][x_pos] = '|'
        elif tile_type == 2:
            screen[y_pos][x_pos] = '#'
        elif tile_type == 3:
            screen[y_pos][x_pos] = '_'
            paddle_x = x_pos
        elif tile_type == 4:
            screen[y_pos][x_pos] = '*'
            ball_x = x_pos

        draw(screen)
    elif program.waiting():
        print('ADDING input!')
        if ball_x < paddle_x:
            print('-1')
            program.add_input(-1)
        elif ball_x > paddle_x:
            print('1')
            program.add_input(1)
        else:
            print('0')
            program.add_input(0)

        program.run_program()

    else:
        print('Never ending story!')
#    break

print(score)

while not program.output_buffer.empty():
    print(program.output_buffer.get())
