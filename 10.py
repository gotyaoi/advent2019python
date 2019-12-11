import itertools
import math

asteroids = set()
with open('../10.txt') as f:
    for y, line in enumerate(f):
        row = []
        for x, c in enumerate(line):
            if c == '#':
                asteroids.add((x, y))

max_x = max(x for x, _ in asteroids)
max_y = max(x for _, y in asteroids)

best = 0
for x, y in asteroids:
    seeable = asteroids.copy()
    seeable.remove((x, y))
    for a, b in list(seeable):
        if (a, b) not in seeable:
            continue
        x_diff = a - x
        y_diff = b - y
        gcd = math.gcd(x_diff, y_diff)
        x_step = x_diff // gcd
        y_step = y_diff // gcd
        for i in range(1, gcd):
            if (x+x_step*i, y+y_step*i) in asteroids:
                a = x + x_step * i
                b = y + y_step * i
                break
        for i in itertools.count(start=1):
            a_step = a + x_step * i
            b_step = b + y_step * i
            if a_step < 0 or a_step > max_x or b_step < 0 or b_step > max_y:
                break
            if (a_step, b_step) in seeable:
                seeable.remove((a_step, b_step))
    count = len(seeable)
    if count > best:
        best = count
print(best)
