from intcode import intcode_v2

with open('../5.txt') as f:
    i = [int(x) for x in f.read().split(',')]

intcode_v2(i)
intcode_v2(i)
