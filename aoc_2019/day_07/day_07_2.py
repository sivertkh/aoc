import sys
import itertools
from queue import SimpleQueue
# --- Day 7: Amplification Circuit ---
# Part 2 -


class IntcodeRunner(object):

    # Halt running at input/output

    def __init__(self, program):
        self.ip = 0
        self.program = program
        self.input_buffer = SimpleQueue()
        self.output_buffer = SimpleQueue()
        self.halted = False

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
                if not self._input():
                    break
            elif opcode == 4:
                self._output(mode)
                break
            elif opcode == 5:
                self._jmp_true(mode)
            elif opcode == 6:
                self._jmp_false(mode)
            elif opcode == 7:
                self._lt(mode)
            elif opcode == 8:
                self._eq(mode)
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

    def _add(self, mode):
        mode = self.adjust_mode(mode, 3)
        param_1 = (self.program[self.program[self.ip+1]]
                   if mode[0] == 0 else self.program[self.ip+1])
        param_2 = (self.program[self.program[self.ip+2]]
                   if mode[1] == 0 else self.program[self.ip+2])
        self.program[self.program[self.ip+3]] = param_1 + param_2

        self.ip += 4

    def _mul(self, mode):
        mode = self.adjust_mode(mode, 3)
        param_1 = (self.program[self.program[self.ip+1]] if mode[0]
                   == 0 else self.program[self.ip+1])
        param_2 = (self.program[self.program[self.ip+2]] if mode[1]
                   == 0 else self.program[self.ip+2])
        self.program[self.program[self.ip+3]] = param_1 * param_2
        self.ip += 4

    def _input(self):
        # Never value mode as we write
        # Throws a queue.empty() if empty. We use this to input values
        if self.input_buffer.empty():
            return False
        self.program[self.program[self.ip+1]] = self.input_buffer.get_nowait()
        self.ip += 2
        return True

    def _output(self, mode):
        mode = self.adjust_mode(mode, 1)
        output = (self.program[self.program[self.ip+1]]
                  if mode[0] == 0 else self.program[self.ip+1])
        self.output_buffer.put(output)
        self.ip += 2

    def _jmp_true(self, mode):
        # Jump if true
        mode = self.adjust_mode(mode, 2)
        jmp = (self.program[self.program[self.ip+1]]
               if mode[0] == 0 else self.program[self.ip+1])
        if jmp > 0:
            self.ip = (self.program[self.program[self.ip+2]]
                       if mode[1] == 0 else self.program[self.ip+2])
        else:
            self.ip += 3

    def _jmp_false(self, mode):
        # Jump if false
        mode = self.adjust_mode(mode, 2)
        jmp = (self.program[self.program[self.ip+1]] if mode[0]
               == 0 else self.program[self.ip+1])
        if jmp == 0:
            self.ip = (self.program[self.program[self.ip+2]]
                       if mode[1] == 0 else self.program[self.ip+2])
        else:
            self.ip += 3

    def _lt(self, mode):
        # less then
        mode = self.adjust_mode(mode, 2)
        param_1 = (self.program[self.program[self.ip+1]]
                   if mode[0] == 0 else self.program[self.ip+1])
        param_2 = (self.program[self.program[self.ip+2]]
                   if mode[1] == 0 else self.program[self.ip+2])

        if param_1 < param_2:
            self.program[self.program[self.ip+3]] = 1
        else:
            self.program[self.program[self.ip+3]] = 0
        self.ip += 4

    def _eq(self, mode):
        # equals
        mode = self.adjust_mode(mode, 2)
        param_1 = (self.program[self.program[self.ip+1]]
                   if mode[0] == 0 else self.program[self.ip+1])
        param_2 = (self.program[self.program[self.ip+2]]
                   if mode[1] == 0 else self.program[self.ip+2])

        if param_1 == param_2:
            self.program[self.program[self.ip+3]] = 1
        else:
            self.program[self.program[self.ip+3]] = 0
        self.ip += 4


with open('./input.txt') as fp:
    program_orign = [int(x) for x in fp.read().split(',') if x]

phase_settings = itertools.permutations([x for x in range(5, 10)])
max_output = 0
max_phase = []
for phase_setting in phase_settings:
    phase_setting = list(phase_setting)
    last_output = 0
    output = 0
    amps = [IntcodeRunner(program_orign.copy()) for _ in range(5)]
    for i, amp in enumerate(amps):
        amp.add_input(phase_setting[i])
    while True:

        if all([amp.halted for amp in amps]):
            break
        for i, amp in enumerate(amps):
            amp.add_input(last_output)
            amp.run_program()
            if amp.halted:
                continue
            last_output = amp.output_buffer.get_nowait()

            if i == 4:
                output = last_output

            if not amp.output_buffer.empty():
                print('To much output...')
                sys.exit(1)

    if output > max_output:
        max_output = output
        max_phase = phase_setting

print(f'max_output: {max_output}')
print(f'max_phase: {max_phase}')

# Part 1..
#print(f'max output: {max_output}, with settings {max_phase}')
#max_output = 0
#max_phase = []
# for phase_setting in phase_settings:
#    phase_setting = list(phase_setting)
#    last_output = 0
#    amps = [IntcodeRunner(program_orign.copy()) for _ in range(5)]
#
#    for i, amp in enumerate(amps):
#        amp.add_input(phase_setting[i])
#        amp.add_input(last_output)
#        amp.run_program()
#        last_output = amp.output_buffer.get_nowait()
#
#        if not amp.output_buffer.empty():
#            print('To much output...')
#            sys.exit(1)
#
#    if last_output > max_output:
#        max_output = last_output
#        max_phase = phase_setting
#
#print(f'max output: {max_output}, with settings {max_phase}')
#
