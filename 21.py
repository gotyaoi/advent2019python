from intcode import intcode_v3, ascii_input, ascii_output

with open('../21.txt') as f:
    instructions = [int(x) for x in f.read().split(',')]

prog = intcode_v3(instructions)

print(''.join(ascii_output(prog)), end='')
program = 'NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nWALK\n'
print(program, end='')
initial = ascii_input(prog, program)
for buf in ascii_output(prog, initial):
    print(buf, end='')
print()

prog = intcode_v3(instructions)

print(''.join(ascii_output(prog)), end='')
program = 'NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nNOT E T\nNOT T T\nOR H T\nAND T J\nRUN\n'
print(program, end='')
initial = ascii_input(prog, program)
for buf in ascii_output(prog, initial):
    print(buf, end='')
print()
