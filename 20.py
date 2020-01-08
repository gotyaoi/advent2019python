import collections
import heapq

maze = []
portals = {}

def add_portal(name, location):
    y, x = location
    if name in portals:
        old = portals.pop(name)
        portals[location] = old
        portals[old] = location
    else:
        portals[name] = location

def make_maze():
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

make_maze()
height = len(maze)
width = len(maze[0])

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

connections = {}

def build_connections():
    vals = portals.values()
    for node in vals:
        subcon = {}
        try:
            oy, ox = node
            if oy == 0 or ox == 0 or oy == height-1 or ox == width-1:
                level_change = -1
            else:
                level_change = 1
            subcon[portals[node]] = (1, level_change)
        except KeyError:
            pass
        to_check = collections.deque([(0, node)])
        seen = set()
        try:
            while True:
                distance, location = to_check.popleft()
                if location in seen:
                    continue
                seen.add(location)
                if location != node and location in vals:
                    subcon[location] = (distance, 0)
                for neighbor in neighbors(location):
                    if maze[neighbor[0]][neighbor[1]] == '.':
                        to_check.append((distance+1, neighbor))
        except IndexError:
            pass
        connections[node] = subcon

build_connections()

def bfs():
    to_check = [(0, portals['AA'])]
    seen = set()
    end = portals['ZZ']
    try:
        while True:
            distance, location = heapq.heappop(to_check)
            if location == end:
                return distance
            if location in seen:
                continue
            seen.add(location)
            for neighbor, (weight, _) in connections[location].items():
                heapq.heappush(to_check, (distance+weight, neighbor))
    except IndexError:
        pass

def bfs2():
    to_check = [(0, 0, portals['AA'])]
    seen = set()
    end = portals['ZZ']
    try:
        while True:
            distance, level, location = heapq.heappop(to_check)
            if level == 0 and location == end:
                return distance
            if (location, level) in seen:
                continue
            seen.add((location, level))
            for neighbor, (weight, level_change) in connections[location].items():
                new_level = level + level_change
                if new_level >= 0:
                    heapq.heappush(to_check, (distance+weight, new_level, neighbor))
    except IndexError:
        pass

print(bfs())
print(bfs2())
