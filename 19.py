import itertools

from intcode import intcode_v3

SAFETY = 10 #may need to increase for shallower beams

with open('../19.txt') as f:
    instructions = [int(x) for x in f.read().split(',')]


def get_lines(start, end, skip_guess = 0, guard = True):
    #skip_guess past the actual end will spin forever
    a = []
    skip = skip_guess
    for i in range(start, end):
        index = i - start
        a.append(['.' for _ in range(skip)])
        started = False
        for j in itertools.count(skip):
            if guard and not started and index != 0 and j - skip > SAFETY:
                break
            drones = intcode_v3(instructions)
            next(drones)
            drones.send(j)
            if drones.send(i):
                a[index].append('#')
                started = True
            else:
                a[index].append('.')
                if started:
                    break
        skip = a[index].index('#') if '#' in a[index] else 0
    return a

def check(row, row_end):
    start = len(row) - 101
    return row[start:start+100].count('#') == 100 == row_end[start:start+100].count('#')

a = get_lines(0, 50)
count = 0
for row in a:
    count += row[:50].count('#')
print(count)

skip = a[-1].index('#')
guess = 64
while True:
    row = get_lines(guess, guess+1, skip, False)[0]
    row_end = get_lines(guess+99, guess+100, row.index('#'), False)[0]
    if check(row, row_end):
        break
    guess = guess * 2
    skip = row.index('#')
low = guess // 2
high = guess
guess = low + (high - low) // 2
while True:
    pass
    row = get_lines(guess, guess+1, skip, False)[0]
    row_end = get_lines(guess+99, guess+100, row.index('#'), False)[0]
    if check(row, row_end):
        high = guess
    else:
        low = guess
    guess = low + (high - low) // 2
    if guess == low:
        guess = high
        break
row = get_lines(guess, guess+1, row.index('#'))[0]
print((row.index('#') + row.count('#') - 100) * 10000 + guess)
