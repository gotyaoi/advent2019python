import copy
import functools
import itertools
import math
import operator

with open('../12.txt') as f:
    positions = ([int(z[2:]) for z in y] for y in [x[1:-2].split(', ') for x in f])
velocities = ([0, 0, 0] for _ in range(4))

moons = tuple(zip(positions, velocities))
moons2 = copy.deepcopy(moons)

def step(moons):
    for (position1, velocity1), (position2, velocity2) in itertools.combinations(moons, 2):
        for i in range(3):
            if position1[i] > position2[i]:
                velocity1[i] -= 1
                velocity2[i] += 1
            elif position1[i] < position2[i]:
                velocity1[i] += 1
                velocity2[i] -= 1
    for (position, velocity) in moons:
        for i in range(3):
            position[i] += velocity[i]

def lcm(*args):
    top = functools.reduce(operator.mul, args, 1)
    length = len(args) - 1
    combos = (functools.reduce(operator.mul, x, 1) for x in itertools.combinations(args, length))
    bottom = functools.reduce(math.gcd, combos, next(combos))
    return top // bottom

for _ in range(1000):
    step(moons)

energy = 0
for (position, velocity) in moons:
    energy += sum(abs(x) for x in position) * sum(abs(x) for x in velocity)
print(energy)

initial = copy.deepcopy(moons2)
#periods = tuple([None, None, None] for _ in range(len(moons2)))
periods = [None, None, None]
for i in itertools.count(start=1):
    step(moons2)
    for j in range(3):
        if periods[j] is None:
            if all(moons2[k][0][j] == initial[k][0][j] and moons2[k][1][j] == initial[k][1][j] for k in range(len(moons))):
                periods[j] = i
    if all(x is not None for x in periods):
        break
print(lcm(*periods))
