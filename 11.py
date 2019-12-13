from intcode import intcode_v3

def robot(i, panels):
    x = 0
    y = 0
    facing = 0
    program = intcode_v3(i)
    next(program)
    try:
        while True:
            panels[(x, y)] = program.send(panels.get((x, y), 0))
            turn = next(program)
            next(program)
            if turn == 0:
                facing = (facing - 1) % 4
            elif turn == 1:
                facing = (facing + 1) % 4
            else:
                raise ValueError
            if facing == 0:
                y += 1
            elif facing == 1:
                x += 1
            elif facing == 2:
                y -= 1
            elif facing == 3:
                x -= 1
            else:
                raise ValueError
    except StopIteration:
        pass

with open('../11.txt') as f:
    i = [int(x) for x in f.read().split(',')]

panels = {}

robot(i, panels)
print(len(panels))

panels = {(0, 0): 1}
robot(i, panels)

xs, ys = zip(*panels)
min_x = min(xs)
transpose_x = 0 - min_x
min_x = 0
max_x = max(xs) + transpose_x
min_y = min(ys)
transpose_y = 0 - min_y
min_y = 0
max_y = max(ys) + transpose_y

array = [[' ' for _ in range(min_x, max_x+1)] for _ in range(min_y, max_y+1)]
for (x, y), v in panels.items():
    array[y+transpose_y][x+transpose_x] = '#' if v else ' '

for line in reversed(array):
    print(''.join(line))
