import collections
import math

asteroids = []
with open('../10.txt') as f:
    for y, line in enumerate(f):
        row = []
        for x, c in enumerate(line):
            if c == '#':
                asteroids.append((x, y))

best = 0
best_angles = None
for x, y in asteroids:
    angles = collections.defaultdict(list)
    for a, b in asteroids:
        if a == x and b == y:
            continue
        x_diff = a - x
        y_diff = b - y
        gcd = math.gcd(x_diff, y_diff)
        x_step = x_diff // gcd
        y_step = y_diff // gcd
        angles[(x_step, y_step)].append((x_diff, y_diff))
    count = len(angles)
    if count > best:
        best = count
        best_angles = angles
print(best)

for points in best_angles.values():
    points.sort(key=lambda x: abs(x[0])+abs(x[1]))
