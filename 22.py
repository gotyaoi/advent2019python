import collections
import functools

stack = collections.deque(x for x in range(10007))

def shuffle(n):
    new = stack.copy()
    position = 0
    for i in range(len(new)):
        stack[position] = (new[i])
        position = (position + n) % 10007

def parse(line):
    if line.startswith('deal into'):
        return stack.reverse
    elif line.startswith('cut'):
        return functools.partial(stack.rotate, -int(line[4:]))
    elif line.startswith('deal with'):
        return functools.partial(shuffle, int(line[20:]))

with open('../22.txt') as f:
    shuffle = [parse(l) for l in f]

for func in shuffle:
    func()

print(stack.index(2019))
