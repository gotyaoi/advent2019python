import heapq
import time

from intcode import intcode_v3

with open('../15.txt') as f:
    i = [int(x) for x in f.read().split(',')]

droid = intcode_v3(i)
next(droid)

def coordinates(base, direction):
    if direction == 1:
        return (base[0], base[1]+1)
    elif direction == 2:
        return (base[0], base[1]-1)
    elif direction == 3:
        return (base[0]-1, base[1])
    elif direction == 4:
        return (base[0]+1, base[1])
    raise ValueError('Bad direction')

def neighbors(bases):
    for base in bases:
        yield (base[0], base[1]+1)
        yield (base[0], base[1]-1)
        yield (base[0]-1, base[1])
        yield (base[0]+1, base[1])

def reverse_path(path):
    for d in reversed(path):
        if d == 1:
            yield 2
        elif d == 2:
            yield 1
        elif d == 3:
            yield 4
        elif d == 4:
            yield 3
        else:
            raise ValueError('Bad direction')

seen = {}
to_check = []
viz = [['X']]
min_x = 0
max_x = 0
min_y = 0
max_y = 0

seen[(0, 0)] = []
heapq.heappush(to_check, (1, ((0, 0), 1)))
heapq.heappush(to_check, (1, ((0, 0), 2)))
heapq.heappush(to_check, (1, ((0, 0), 3)))
heapq.heappush(to_check, (1, ((0, 0), 4)))

while to_check:
    _, (node, direction) = heapq.heappop(to_check)
    path = seen[node]
    for d in path:
        droid.send(d)
        next(droid)
    result = droid.send(direction)
    next(droid)
    new_node = coordinates(node, direction)

    if new_node[0] < min_x:
        for row in viz:
            row.insert(0, '?')
        min_x = new_node[0]
    elif new_node[0] > max_x:
        for row in viz:
            row.append('?')
        max_x = new_node[0]
    if new_node[1] < min_y:
        viz.append(['?']*(max_x-min_x+1))
        min_y = new_node[1]
    elif new_node[1] > max_y:
        viz.insert(0, ['?']*(max_x-min_x+1))
        max_y = new_node[1]

    if result == 0:
        viz[max_y-new_node[1]][new_node[0]-min_x] = 'O'
        for d in reverse_path(path):
            droid.send(d)
            next(droid)
    elif result == 1:
        viz[max_y-new_node[1]][new_node[0]-min_x] = ' '
        if new_node not in seen:
            seen[new_node] = path[:] + [direction]
            if direction != 2:
                heapq.heappush(to_check, (len(path)+2, (new_node, 1)))
            if direction != 1:
                heapq.heappush(to_check, (len(path)+2, (new_node, 2)))
            if direction != 4:
                heapq.heappush(to_check, (len(path)+2, (new_node, 3)))
            if direction != 3:
                heapq.heappush(to_check, (len(path)+2, (new_node, 4)))
        for d in reverse_path(seen[new_node]):
            droid.send(d)
            next(droid)
    elif result == 2:
        system = new_node
        distance = len(path) + 1
        viz[max_y-new_node[1]][new_node[0]-min_x] = 'Z'
    else:
        raise ValueError('Bad result')
    print()
    for row in viz:
        print(''.join(row))

minutes = 0
adjacent = [(x, y) for x, y in neighbors([system]) if viz[max_y-y][x-min_x] == ' ']
while adjacent:
    minutes += 1
    for x, y in adjacent:
        viz[max_y-y][x-min_x] = 'Z'
    adjacent = [(x, y) for x, y in neighbors(adjacent) if viz[max_y-y][x-min_x] == ' ']
    print()
    for row in viz:
        print(''.join(row))
    time.sleep(0.1)

print('Oxygen system at location', system, '\ndistance', distance)
print(minutes, 'minutes to pressurize the area')
