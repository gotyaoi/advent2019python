from intcode import intcode_v3

with open('../17.txt') as f:
    instructions = [int(x) for x in f.read().split(',')]

prog = intcode_v3(instructions)

scaffolds = [[]]
try:
    while True:
        output = chr(next(prog))
        if output == '.':
            scaffolds[-1].append(False)
        elif output in ['#', '^', 'v', '<', '>']:
            scaffolds[-1].append(True)
        elif output == '\n':
            scaffolds.append([])
        else:
            raise ValueError('Bad output')
        print(output, end='')
except StopIteration:
    pass
while not scaffolds[-1]:
    del scaffolds[-1]

width = len(scaffolds[0])
height = len(scaffolds)

def interest(x, y):
    yield (x, y)
    yield (x+1, y)
    yield (x-1, y)
    yield (x, y+1)
    yield (x, y-1)

s = 0
for i in range(height):
    if i == 0 or i == height-1:
        continue
    for j in range(width):
        if j == 0 or j == width-1:
            continue
        if not all(scaffolds[y][x] for x, y in interest(j, i)):
            continue
        s += i*j

print(s)

instructions[0] = 2

prog = intcode_v3(instructions)
try:
    programs = [[ord(c) for c in l]
                 for l in ['A,B,A,C,A,B,C,B,C,B\n',
                           'R,8,L,10,L,12,R,4\n',
                           'R,8,L,12,R,4,R,4\n',
                           'R,8,L,10,R,8\n',
                           'n\n']]
    output = next(prog)
    for program in programs:
        while output is not None:
            print(chr(output), end='')
            output = next(prog)
        for i in program:
            output = prog.send(i)
    output = next(prog)
    while output is not None:
        if output < 128:
            print(chr(output), end='')
        else:
            print(output)
        output = next(prog)
except StopIteration:
    pass
