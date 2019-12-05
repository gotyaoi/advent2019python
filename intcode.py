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
        code = i[pc]
        opcode = code % 100
        if opcode == 1:
            if (code // 100) % 10:
                parameter1 = i[pc+1]
            else:
                parameter1 = i[i[pc+1]]
            if (code // 1000) % 10:
                parameter2 = i[pc+2]
            else:
                parameter2 = i[i[pc+2]]
            i[i[pc+3]] = parameter1 + parameter2
            pc += 4
        elif opcode == 2:
            if (code // 100) % 10:
                parameter1 = i[pc+1]
            else:
                parameter1 = i[i[pc+1]]
            if (code // 1000) % 10:
                parameter2 = i[pc+2]
            else:
                parameter2 = i[i[pc+2]]
            i[i[pc+3]] = parameter1 * parameter2
            pc += 4
        elif opcode == 3:
            i[i[pc+1]] = int(input())
            pc += 2
        elif opcode == 4:
            if (code // 100) % 10:
                parameter1 = i[pc+1]
            else:
                parameter1 = i[i[pc+1]]
            print(parameter1)
            pc += 2
        elif opcode == 5:
            if (code // 100) % 10:
                parameter1 = i[pc+1]
            else:
                parameter1 = i[i[pc+1]]
            if parameter1 != 0:
                if (code // 1000) % 10:
                    parameter2 = i[pc+2]
                else:
                    parameter2 = i[i[pc+2]]
                pc = parameter2
            else:
                pc += 3
        elif opcode == 6:
            if (code // 100) % 10:
                parameter1 = i[pc+1]
            else:
                parameter1 = i[i[pc+1]]
            if parameter1 == 0:
                if (code // 1000) % 10:
                    parameter2 = i[pc+2]
                else:
                    parameter2 = i[i[pc+2]]
                pc = parameter2
            else:
                pc += 3
        elif opcode == 7:
            if (code // 100) % 10:
                parameter1 = i[pc+1]
            else:
                parameter1 = i[i[pc+1]]
            if (code // 1000) % 10:
                parameter2 = i[pc+2]
            else:
                parameter2 = i[i[pc+2]]
            if parameter1 < parameter2:
                i[i[pc+3]] = 1
            else:
                i[i[pc+3]] = 0
            pc += 4
        elif opcode == 8:
            if (code // 100) % 10:
                parameter1 = i[pc+1]
            else:
                parameter1 = i[i[pc+1]]
            if (code // 1000) % 10:
                parameter2 = i[pc+2]
            else:
                parameter2 = i[i[pc+2]]
            if parameter1 == parameter2:
                i[i[pc+3]] = 1
            else:
                i[i[pc+3]] = 0
            pc += 4
        elif opcode == 99:
            break
        else:
            raise ValueError
    return i[0]
