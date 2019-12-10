import itertools

from intcode import intcode_v3

with open('../9.txt') as f:
    i = [int(x) for x in f.read().split(',')]

    test = intcode_v3(i)
    next(test)
    print(test.send(1))
    try:
        while True:
            print(next(test))
    except StopIteration:
        pass

    test = intcode_v3(i)
    next(test)
    print(test.send(2))
