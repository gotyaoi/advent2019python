import collections
import copy
import heapq

facility = []
starts = {}
with open('../18.txt') as f:
    for i, line in enumerate(f):
        row = []
        facility.append(row)
        for j, c in enumerate(list(line[:-1])):
            row.append(c)
            #row.append(ord(c))
            if c == '@' or 'a' <= c <= 'z':
                starts[c] = (i, j)

max_y = i
max_x = j

def neighbors(y, x):
    if y != 0:
        yield (y-1, x)
    if y != max_y:
        yield (y+1, x)
    if x != 0:
        yield (y, x-1)
    if x != max_x:
        yield (y, x+1)

def bfs_make_connections():
    connections = collections.defaultdict(dict)
    for node, start in starts.items():
        seen = {start}
        # all edges have "weight" of one so a queue works better than a minheap.
        to_check = collections.deque((1, x, []) for x in neighbors(*start))
        try:
            while True:
                distance, location, intermediates = to_check.popleft()
                if location in seen:
                    continue
                seen.add(location)
                y, x = location
                tile = facility[y][x]
                if tile == '#':
                    continue
                elif 'a' <= tile <= 'z':
                    connections[node][tile] = (distance, intermediates)
                    intermediates = intermediates[:] + [tile]
                elif 'A' <= tile <= 'Z':
                    intermediates = intermediates[:] + [tile]
                for neighbor in neighbors(y, x):
                    to_check.append((distance+1, neighbor, intermediates))
        except IndexError:
            pass
    return dict(connections)

def bfs(connections):
    to_check = [(0, ('@',), set())]
    length = len(connections)
    best = []
    best_dict = {} # this is the key
    try:
        while True:
            distance, path, collected = heapq.heappop(to_check)
            for neighbor, (neighbor_distance, intermediates) in connections[path[-1]].items():
                if any((x not in collected and x.lower() not in collected) for x in intermediates) or neighbor in collected:
                    continue
                next_distance = distance + neighbor_distance
                next_path = path + (neighbor,)
                if len(next_path) == length:
                    best.append((next_distance, next_path))
                    continue
                next_collected = collected.copy()
                next_collected.add(neighbor)
                best_key = (next_path[-1], tuple(next_collected))
                if best_key in best_dict and next_distance >= best_dict[best_key]:
                    pass
                else:
                    heapq.heappush(to_check, (next_distance, next_path, next_collected))
                    best_dict[best_key] = next_distance
    except IndexError:
        pass
    print(min(best))

connections = bfs_make_connections()
bfs(connections)

def bfs_quad(connections):
    to_check = [(0, (('1',), ('2',), ('3',), ('4',)), set())]
    length = len(connections)
    best = []
    best_dict = {} # this is the key
    try:
        while True:
            distance, paths, collected = heapq.heappop(to_check)
            for robot, path in enumerate(paths):
                for neighbor, (neighbor_distance, intermediates) in connections[path[-1]].items():
                    if any((x not in collected and x.lower() not in collected) for x in intermediates) or neighbor in collected:
                        continue
                    next_distance = distance + neighbor_distance
                    next_path = path + (neighbor,)
                    next_paths = (next_path if robot == 0 else paths[0],
                                  next_path if robot == 1 else paths[1],
                                  next_path if robot == 2 else paths[2],
                                  next_path if robot == 3 else paths[3])
                    if len(next_paths[0]) + len(next_paths[1]) + len(next_paths[2]) + len(next_paths[3]) == length:
                        best.append((next_distance, next_paths))
                        continue
                    next_collected = collected.copy()
                    next_collected.add(neighbor)
                    best_key = ((next_paths[0][-1], next_paths[1][-1], next_paths[2][-1], next_paths[3][-1]), tuple(next_collected))
                    if best_key in best_dict and next_distance >= best_dict[best_key]:
                        pass
                    else:
                        heapq.heappush(to_check, (next_distance, next_paths, next_collected))
                        best_dict[best_key] = next_distance
    except IndexError:
        pass
    print(min(best))

facility[39][39:42] = '1#2'
facility[40][39:42] = '###'
facility[41][39:42] = '3#4'
del starts['@']
starts['1'] = (39, 39)
starts['2'] = (39, 41)
starts['3'] = (41, 39)
starts['4'] = (41, 41)

connections = bfs_make_connections()
bfs_quad(connections)
