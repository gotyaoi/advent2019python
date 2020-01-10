def intcode_v1(i):
    i = i[:]
    pc = 0
    while True:
        opcode = i[pc]
        if opcode == 1:
            i[i[pc+3]] = i[i[pc+1]] + i[i[pc+2]]
            pc += 4
        elif opcode == 2:
            i[i[pc+3]] = i[i[pc+1]] * i[i[pc+2]]
            pc += 4
        elif opcode == 99:
            break
        else:
            raise ValueError
    return i[0]

def intcode_v2(i):
    i = i[:]
    pc = 0
    while True:
        opcode, parameters, dest = decode(i, pc)
        if opcode == 1:
            i[dest] = parameters[0] + parameters[1]
            pc += 4
        elif opcode == 2:
            i[dest] = parameters[0] * parameters[1]
            pc += 4
        elif opcode == 3:
            i[dest] = int(input())
            pc += 2
        elif opcode == 4:
            print(parameters[0])
            pc += 2
        elif opcode == 5:
            if parameters[0] != 0:
                pc = parameters[1]
            else:
                pc += 3
        elif opcode == 6:
            if parameters[0] == 0:
                pc = parameters[1]
            else:
                pc += 3
        elif opcode == 7:
            if parameters[0] < parameters[1]:
                i[dest] = 1
            else:
                i[dest] = 0
            pc += 4
        elif opcode == 8:
            if parameters[0] == parameters[1]:
                i[dest] = 1
            else:
                i[dest] = 0
            pc += 4
        elif opcode == 99:
            break
        else:
            raise ValueError
    return i[0]

NUM_PARAMS = {1: 2, 2: 2,
              3: 0, 4: 1,
              5: 2, 6: 2,
              7: 2, 8: 2,
              9: 1, 99: 0}

def decode(i, pc, offset=0):
    code = i[pc]
    opcode = code % 100
    num = NUM_PARAMS[opcode]
    parameters = []
    for j in range(1, num+1):
        pos = 10 * 10**j
        mode = (code // pos) % 10
        if mode == 1:
            parameters.append(i[pc+j])
        elif mode == 2:
            index = i[pc+j] + offset
            if index >= len(i):
                parameters.append(0)
            else:
                parameters.append(i[index])
        else:
            index = i[pc+j]
            if index >= len(i):
                parameters.append(0)
            else:
                parameters.append(i[index])
    dest = 0
    if opcode in (1, 2, 3, 7, 8):
        pos = 10 * 10**(num+1)
        mode = (code // pos) % 10
        if mode == 1:
            raise ValueError
        elif mode == 2:
            dest = i[pc+num+1] + offset
        else:
            dest = i[pc+num+1]
        if dest >= len(i):
            needed = dest - len(i) + 1
            for _ in range(needed):
                i.append(0);
    return opcode, parameters, dest

def intcode_v3(i):
    i = i[:]
    pc = 0
    offset = 0
    while True:
        opcode, parameters, dest = decode(i, pc, offset)
        if opcode == 1:
            i[dest] = parameters[0] + parameters[1]
            pc += 4
        elif opcode == 2:
            i[dest] = parameters[0] * parameters[1]
            pc += 4
        elif opcode == 3:
            i[dest] = yield None
            pc += 2
        elif opcode == 4:
            yield parameters[0]
            pc += 2
        elif opcode == 5:
            if parameters[0] != 0:
                pc = parameters[1]
            else:
                pc += 3
        elif opcode == 6:
            if parameters[0] == 0:
                pc = parameters[1]
            else:
                pc += 3
        elif opcode == 7:
            if parameters[0] < parameters[1]:
                i[dest] = 1
            else:
                i[dest] = 0
            pc += 4
        elif opcode == 8:
            if parameters[0] == parameters[1]:
                i[dest] = 1
            else:
                i[dest] = 0
            pc += 4
        elif opcode == 9:
            offset += parameters[0]
            pc += 2
        elif opcode == 99:
            break
        else:
            raise ValueError

def ascii_input(prog, data):
    for i in [ord(c) for c in data]:
        output = prog.send(i)
    return output

def ascii_output(prog, initial=None):
    if initial is None:
        output = next(prog)
    else:
        output = initial
    ret = []
    try:
        while output is not None:
            if output < 128:
                ret.append(chr(output))
                if ret[-1] == '\n':
                    yield ''.join(ret)
                    ret.clear()
            else:
                ret.append(str(output))
            output = next(prog)
    except StopIteration:
        pass
    yield ''.join(ret)
