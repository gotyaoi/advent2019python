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
        opcode, parameters = decode(i, pc)
        if opcode == 1:
            i[i[pc+3]] = parameters[0] + parameters[1]
            pc += 4
        elif opcode == 2:
            i[i[pc+3]] = parameters[0] * parameters[1]
            pc += 4
        elif opcode == 3:
            i[i[pc+1]] = int(input())
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
                i[i[pc+3]] = 1
            else:
                i[i[pc+3]] = 0
            pc += 4
        elif opcode == 8:
            if parameters[0] == parameters[1]:
                i[i[pc+3]] = 1
            else:
                i[i[pc+3]] = 0
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
              99: 0}

def decode(i, pc):
    code = i[pc]
    opcode = code % 100
    num = NUM_PARAMS[opcode]
    parameters = []
    for j in range(1, num+1):
        pos = 10 * 10**j
        if (code // pos) % 10:
            parameters.append(i[pc+j])
        else:
            parameters.append(i[i[pc+j]])
    return opcode, parameters

def intcode_v3(i):
    i = i[:]
    pc = 0
    while True:
        opcode, parameters = decode(i, pc)
        if opcode == 1:
            i[i[pc+3]] = parameters[0] + parameters[1]
            pc += 4
        elif opcode == 2:
            i[i[pc+3]] = parameters[0] * parameters[1]
            pc += 4
        elif opcode == 3:
            i[i[pc+1]] = yield None
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
                i[i[pc+3]] = 1
            else:
                i[i[pc+3]] = 0
            pc += 4
        elif opcode == 8:
            if parameters[0] == parameters[1]:
                i[i[pc+3]] = 1
            else:
                i[i[pc+3]] = 0
            pc += 4
        elif opcode == 99:
            break
        else:
            raise ValueError
