import collections
import itertools

eris = []
with open('../24.txt') as f:
    for line in f:
        bugline = []
        for char in line:
            if char == '#':
                bugline.append(True)
            elif char == '.':
                bugline.append(False)
            else:
                pass
        eris.append(tuple(bugline))
eris = tuple(eris)
height = len(eris)
bottom = height - 1
mid_down = bottom // 2
width = len(eris[0])
right = width - 1
mid_side = right // 2

def iterate(bugs):
    new = []
    for y in range(height):
        bugline = []
        for x in range(width):
            count = 0
            if y != 0:
                if bugs[y-1][x]:
                    count += 1
            if y != bottom:
                if bugs[y+1][x]:
                    count += 1
            if x != 0:
                if bugs[y][x-1]:
                    count += 1
            if x != right:
                if bugs[y][x+1]:
                    count += 1
            if bugs[y][x]:
                if count == 1:
                    bugline.append(True)
                else:
                    bugline.append(False)
            else:
                if count == 1 or count == 2:
                    bugline.append(True)
                else:
                    bugline.append(False)
        new.append(tuple(bugline))
    return tuple(new)

def empty_level():
    return tuple(tuple(False for x in range(width)) for y in range(height))

actual_eris = collections.deque([empty_level(), eris, empty_level()])

def iterate2(actual_bugs):
    last = len(actual_bugs) - 1
    new = collections.deque()
    for i in range(len(actual_bugs)):
        new_level = []
        for y in range(height):
            bugline = []
            for x in range(width):
                if y == mid_down and x == mid_side:
                    bugline.append(False)
                    continue
                count = 0
                if y == 0:
                    if i != 0:
                        if actual_bugs[i-1][mid_down-1][mid_side]:
                            count += 1
                elif y == mid_down+1 and x == mid_side:
                    if i != last:
                        for j in range(width):
                            if actual_bugs[i+1][bottom][j]:
                                count += 1
                else:
                    if actual_bugs[i][y-1][x]:
                        count += 1
                if y == mid_down-1 and x == mid_side:
                    if i != last:
                        for j in range(width):
                            if actual_bugs[i+1][0][j]:
                                count += 1
                elif y == bottom:
                    if i != 0:
                        if actual_bugs[i-1][mid_down+1][mid_side]:
                            count += 1
                else:
                    if actual_bugs[i][y+1][x]:
                        count += 1
                if x == 0:
                    if i != 0:
                        if actual_bugs[i-1][mid_down][mid_side-1]:
                            count += 1
                elif x == mid_side+1 and y == mid_down:
                    if i != last:
                        for j in range(height):
                            if actual_bugs[i+1][j][right]:
                                count += 1
                else:
                    if actual_bugs[i][y][x-1]:
                        count += 1
                if x == mid_side-1 and y == mid_down:
                    if i != last:
                        for j in range(height):
                            if actual_bugs[i+1][j][0]:
                                count += 1
                elif x == right:
                    if i != 0:
                        if actual_bugs[i-1][mid_down][mid_side+1]:
                            count += 1
                else:
                    if actual_bugs[i][y][x+1]:
                        count += 1
                if actual_bugs[i][y][x]:
                    if count == 1:
                        bugline.append(True)
                    else:
                        bugline.append(False)
                else:
                    if count == 1 or count == 2:
                        bugline.append(True)
                    else:
                        bugline.append(False)
            new_level.append(tuple(bugline))
        new.append(tuple(new_level))
    if any(itertools.chain.from_iterable(new[0])):
        new.appendleft(empty_level())
    if any(itertools.chain.from_iterable(new[-1])):
        new.append(empty_level())
    return new

seen = {eris}
while True:
    eris = iterate(eris)
    if eris in seen:
        break
    seen.add(eris)

biodiversity = 0
for y in range(height):
    for x in range(width):
        if eris[y][x]:
            power = y * 5 + x
            biodiversity += 2**power
print(biodiversity)

for _ in range(200):
    actual_eris = iterate2(actual_eris)

print(sum(itertools.chain.from_iterable(itertools.chain.from_iterable(x) for x in actual_eris)))
