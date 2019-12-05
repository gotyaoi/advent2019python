from intcode import intcode_v1

with open('../2.txt') as f:
    i = [int(x) for x in f.read().split(',')]

i[1] = 12
i[2] = 2

print(intcode_v1(i))

from itertools import product

for a, b in product(range(100), range(100)):
    i[1] = a
    i[2] = b
    if intcode_v1(i) == 19690720:
        print(100 * a + b)
        break
