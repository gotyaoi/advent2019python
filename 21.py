from intcode import intcode_v3

with open('../21.txt') as f:
    instructions = [int(x) for x in f.read().split(',')]

prog = intcode_v3(instructions)

try:
    output = next(prog)
    while output is not None:
        print(chr(output), end='')
        output = next(prog)
    program = [ord(c) for c in 'NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nWALK\n']
    for i in program:
        output = prog.send(i)
    while output is not None:
        if output < 128:
            print(chr(output), end='')
        else:
            print(output)
        output = next(prog)
except StopIteration:
    pass

prog = intcode_v3(instructions)

try:
    output = next(prog)
    while output is not None:
        print(chr(output), end='')
        output = next(prog)
    program = [ord(c) for c in 'NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nNOT E T\nNOT T T\nOR H T\nAND T J\nRUN\n']
    for i in program:
        output = prog.send(i)
    while output is not None:
        if output < 128:
            print(chr(output), end='')
        else:
            print(output)
        output = next(prog)
except StopIteration:
    pass
