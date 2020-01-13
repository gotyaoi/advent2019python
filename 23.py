import collections

from intcode import intcode_v3

with open('../23.txt') as f:
    instructions = [int(x) for x in f.read().split(',')]

prog = intcode_v3(instructions)
computers = []
inputs = []
outputs = []
for i in range(50):
    computers.append(intcode_v3(instructions))
    inputs.append(collections.deque())
    next(computers[-1])
    outputs.append(computers[-1].send(i))

nat = None
nat_sent = None
while True:
    for i in range(50):
        if outputs[i] is None:
            try:
                x, y = inputs[i].popleft()
                computers[i].send(x)
                outputs[i] = computers[i].send(y)
            except IndexError:
                outputs[i] = computers[i].send(-1)
        else:
            x = next(computers[i])
            y = next(computers[i])
            if outputs[i] == 255:
                if nat is None:
                    print(y)
                nat = (x, y)
            else:
                inputs[outputs[i]].append((x, y))
            outputs[i] = next(computers[i])
    if all(x is None for x in outputs) and all(not x for x in inputs):
        inputs[0].append(nat)
        if nat_sent is not None and nat[1] == nat_sent[1]:
            print(nat[1])
            break
        else:
            nat_sent = nat
