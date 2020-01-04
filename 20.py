import collections

maze = []
portals = {}

def add_portal(name, location):
    y, x = location
    if name in portals:
        old = portals.pop(name)
        portals[location] = old
        portals[old] = location
    else:
        portals[name] = (location)

with open('../20.txt') as f:
    first = None
    second = None
    seen = {}
    for i, line in enumerate(f, start=-2):
        length = len(line) - 5
        if line[2] == '#' or line[2] == '.':
            maze.append([])
            for j, c in enumerate(line[:-1], start = -2):
                if c == '#' or c == '.':
                    maze[-1].append(c)
                elif c == ' ':
                    if 0 <= j < length:
                        maze[-1].append(c)
                elif (i, j-1) in seen:
                    if 0 <= j < length:
                        maze[-1].append(' ')
                    name = seen.pop((i, j-1)) + c
                    if line[j] != '.':
                        add_portal(name, (i, j+1))
                    else:
                        add_portal(name, (i, j-2))
                elif (i-1, j) in seen:
                    maze[-1].append(' ')
                    name = seen.pop((i-1, j)) + c
                    if maze[i-2][j] == '.':
                        add_portal(name, (i-2, j))
                    else:
                        add_portal(name, (i+1, j))
                else:
                    if 0 <= j < length:
                        maze[-1].append(' ')
                    seen[(i, j)] = c
        else:
            if first is None:
                first = line[:-1]
            else:
                second = line[:-1]
                for j, (c1, c2) in enumerate(zip(first, second), start = -2):
                    if c1 != ' ':
                        name = c1 + c2
                        if i == -1:
                            target = 0
                        else:
                            target = i-2
                        add_portal(name, (target, j))
                first = None
                second = None

height = len(maze)
width = len(maze[0])

solid = True
for i in range(height):
    if solid:
        if maze[i][width//2] == ' ':
            solid = False
            inner_top = i-1
    else:
        if maze[i][width//2] == '.' or maze[i][width//2] == '#':
            inner_bottom = i
            break
solid = True
for i in range(width):
    if solid:
        if maze[height//2][i] == ' ':
            solid = False
            inner_left = i-1
    else:
        if maze[height//2][i] == '.' or maze[height//2][i] == '#':
            inner_right = i
            break

real_portals = {}
for origin, destination in portals.items():
    if origin == 'AA' or origin == 'ZZ':
        continue
    oy, ox = origin
    if oy == 0 or ox == 0 or oy == height-1 or ox == width-1:
        real_portals[origin] = (destination, -1)
    else:
        real_portals[origin] = (destination, 1)

def neighbors(location):
    y, x = location
    if y > 0:
        yield (y-1, x)
    if y < height-1:
        yield (y+1, x)
    if x > 0:
        yield (y, x-1)
    if x < width-1:
        yield (y, x+1)

def bfs():
    to_check = collections.deque([(0, portals['AA'])])
    seen = set()
    end = portals['ZZ']
    try:
        while True:
            distance, location = to_check.popleft()
            if location in seen:
                continue
            seen.add(location)
            for neighbor in neighbors(location):
                if neighbor == end:
                    return distance + 1
                if maze[neighbor[0]][neighbor[1]] == '.':
                    to_check.append((distance+1, neighbor))
            if location in portals:
                to_check.append((distance+1, portals[location]))
    except IndexError:
        pass

def bfs2():
    to_check = collections.deque([(0, 0, portals['AA'])])
    seen = set()
    end = portals['ZZ']
    try:
        while True:
            distance, level, location = to_check.popleft()
            if (location, level) in seen:
                continue
            seen.add((location, level))
            for neighbor in neighbors(location):
                if level == 0 and neighbor == end:
                    return distance + 1
                if maze[neighbor[0]][neighbor[1]] == '.':
                    to_check.append((distance+1, level, neighbor))
            if location in real_portals:
                destination, level_change = real_portals[location]
                new_level = level + level_change
                if new_level >= 0:
                    to_check.append((distance+1, new_level, destination))
    except IndexError:
        pass

print(bfs())
print(bfs2())
