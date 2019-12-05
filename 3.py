with open('../3.txt') as f:
    wire1 = [(x[0], int(x[1:])) for x in f.readline().split(',')]
    wire2 = [(x[0], int(x[1:])) for x in f.readline().split(',')]

wire1_dict = {}
wire2_dict = {}

pos_x = 0
pos_y = 0
distance = 0
for direction, length in wire1:
    if direction == 'U':
        for i in range(length):
            pos_y += 1
            distance += 1
            wire1_dict[(pos_x, pos_y)] = distance
    elif direction == 'R':
        for i in range(length):
            pos_x += 1
            distance += 1
            wire1_dict[(pos_x, pos_y)] = distance
    elif direction == 'D':
        for i in range(length):
            pos_y -= 1
            distance += 1
            wire1_dict[(pos_x, pos_y)] = distance
    else:
        for i in range(length):
            pos_x -= 1
            distance += 1

pos_x = 0
pos_y = 0
distance = 0
for direction, length in wire2:
    if direction == 'U':
        for i in range(length):
            pos_y += 1
            distance += 1
            wire2_dict[(pos_x, pos_y)] = distance
    elif direction == 'R':
        for i in range(length):
            pos_x += 1
            distance += 1
            wire2_dict[(pos_x, pos_y)] = distance
    elif direction == 'D':
        for i in range(length):
            pos_y -= 1
            distance += 1
            wire2_dict[(pos_x, pos_y)] = distance
    else:
        for i in range(length):
            pos_x -= 1
            distance += 1
            wire2_dict[(pos_x, pos_y)] = distance

crossings = wire1_dict.keys() & wire2_dict.keys()

x, y = crossings.pop()
best = abs(x) + abs(y)
for x, y in crossings:
    distance = abs(x) + abs(y)
    if distance < best:
        best = distance
print(best)

crossings = wire1_dict.keys() & wire2_dict.keys()

crossing = crossings.pop()
best = wire1_dict[crossing] + wire2_dict[crossing]
for crossing in crossings:
    distance = wire1_dict[crossing] + wire2_dict[crossing]
    if distance < best:
        best = distance
print(best)
