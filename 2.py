def intcode(i):
    i = i[:]
    pc = 0
    while True:
        opcode = i[pc]
        if opcode == 1:
            i[i[pc+3]] = i[i[pc+1]] + i[i[pc+2]]
            pc += 4
        elif opcode == 2:
            i[i[pc+3]] = i[i[pc+1]] * i[i[pc+2]]
            pc += 4
        elif opcode == 99:
            break
        else:
            raise ValueError
    return i[0]

with open('../2.txt') as f:
    i = [int(x) for x in f.read().split(',')]

i[1] = 12
i[2] = 2

print(intcode(i))

from itertools import product

for a, b in product(range(100), range(100)):
    i[1] = a
    i[2] = b
    if intcode(i) == 19690720:
        print(100 * a + b)
        break
