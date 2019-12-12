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
best_coordinates = None
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
        key = math.atan2(y_step, x_step)-math.pi/2
        if y_step < 0 and x_step < 0:
            diff = key + math.pi
            key = -key + (2*diff)
        angles[key].append((x_diff, y_diff))
    count = len(angles)
    if count > best:
        best = count
        best_coordinates = (x, y)
        best_angles = angles
print(best)

for points in best_angles.values():
    points.sort(key=lambda x: abs(x[0])+abs(x[1]))

i = 0
while True:
    for angle in sorted(best_angles.keys()):
        line = best_angles[angle]
        asteroid = line.pop(0)
        i += 1
        if not line:
            del best_angles[angle]
        if i == 200:
            break
    if i == 200:
        break
print((asteroid[0]+best_coordinates[0])*100+(asteroid[1]+best_coordinates[1]))
