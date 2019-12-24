import collections
import math

with open('../14.txt') as f:
    reactions = {pair[1][pair[1].index(' ')+1:-1]:
                    (int(pair[1][:pair[1].index(' ')]),
                     tuple((comp[comp.index(' ')+1:], int(comp[:comp.index(' ')]))
                        for comp in pair[0].split(', ')))
                            for pair in [line.split(' => ') for line in f]}

def make_fuel(n):
    leftovers = collections.defaultdict(int)
    required = [(name, amount*n) for name, amount in reactions['FUEL'][1]]
    ore = 0
    try:
        while True:
            name, amount = required.pop()
            leftover = leftovers[name]
            if leftover >= amount:
                leftovers[name] -= amount
                continue
            elif leftover > 0:
                amount -= leftover
            output, formula = reactions[name]
            multiplier = math.ceil(amount/output)
            leftovers[name] = output*multiplier-amount
            for name, amount in formula:
                amount = amount*multiplier
                #used[name] += amount
                if name == 'ORE':
                    ore += amount
                    continue
                required.append((name, amount))
    except IndexError:
        pass
    return ore

ore = make_fuel(1)
print(ore)

lower = (1, ore)
upper = (2, make_fuel(2))

while upper[1] <= 1000000000000:
    lower = upper
    new_up = upper[0]*2
    upper = (new_up, make_fuel(new_up))

good = lower
while True:
    new_can = lower[0]+(upper[0]-lower[0])//2
    candidate = (new_can, make_fuel(new_can))
    if candidate[1] <= 1000000000000:
        if candidate == good:
            break
        good = candidate
        lower = candidate
    else:
        upper = candidate
print(good[0])
