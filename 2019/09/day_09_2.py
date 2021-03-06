import sys
import itertools
from queue import SimpleQueue
# --- Day 9: Sensor Boost ---
# Part 2 - ok


class IntcodeRunner(object):

    # Halt running at input/output

    def __init__(self, program, break_on_output=False):
        self.ip = 0
        self.relative_base = 0
        self.program = program + [0 for _ in range(1000)]
        self.input_buffer = SimpleQueue()
        self.output_buffer = SimpleQueue()
        self.halted = False
        self.break_on_output = break_on_output

    def add_input(self, input):
        self.input_buffer.put(input)

    def run_program(self):
        if self.halted:
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
                if not self._input(mode):
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
                self.halted = True
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
        if self.input_buffer.empty():
            return False
        self.write_mode_value(mode[0], 1, self.input_buffer.get_nowait())
        self.ip += 2
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


with open('./input.txt') as fp:
    program_orign = [int(x) for x in fp.read().split(',') if x]

program = IntcodeRunner(program_orign.copy())

program.add_input(2)
program.run_program()
output = []
while not program.output_buffer.empty():
    output.append(program.output_buffer.get_nowait())

print(output)
