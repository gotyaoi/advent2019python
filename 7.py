import itertools

from intcode import intcode_v3

with open('../7.txt') as f:
    i = [int(x) for x in f.read().split(',')]

best = 0
for (pA, pB, pC, pD, pE) in itertools.permutations((0, 1, 2, 3, 4)):
    ampA = intcode_v3(i)
    next(ampA)
    ampA.send(pA)
    ampB = intcode_v3(i)
    next(ampB)
    ampB.send(pB)
    ampC = intcode_v3(i)
    next(ampC)
    ampC.send(pC)
    ampD = intcode_v3(i)
    next(ampD)
    ampD.send(pD)
    ampE = intcode_v3(i)
    next(ampE)
    ampE.send(pE)

    oA = ampA.send(0)
    oB = ampB.send(oA)
    oC = ampC.send(oB)
    oD = ampD.send(oC)
    oE = ampE.send(oD)
    if oE > best:
        best = oE

print(best)

best = 0
for (pA, pB, pC, pD, pE) in itertools.permutations((5, 6, 7, 8, 9)):
    ampA = intcode_v3(i)
    next(ampA)
    ampA.send(pA)
    ampB = intcode_v3(i)
    next(ampB)
    ampB.send(pB)
    ampC = intcode_v3(i)
    next(ampC)
    ampC.send(pC)
    ampD = intcode_v3(i)
    next(ampD)
    ampD.send(pD)
    ampE = intcode_v3(i)
    next(ampE)
    ampE.send(pE)

    oE = 0
    try:
        while True:
            oA = ampA.send(oE)
            oB = ampB.send(oA)
            oC = ampC.send(oB)
            oD = ampD.send(oC)
            oE = ampE.send(oD)
            next(ampA)
            next(ampB)
            next(ampC)
            next(ampD)
            next(ampE)
    except StopIteration:
        if oE > best:
            best = oE

print(best)
