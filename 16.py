import itertools

with open('../16.txt') as f:
    sequence = [int(x) for x in f.read()[:-1]]

def pattern(n):
    base = [0, 1, 0, -1]
    for part in itertools.cycle(base):
        for _ in range(n):
            yield part

def phase(s):
    output = []
    for i, b in enumerate(s, start=1):
        pat = pattern(i)
        next(pat)
        output.append(abs(sum(a*b for a, b in zip(s, pat)))%10)
    return output

seq = sequence[:]
for i in range(100):
    print(i)
    seq = phase(seq)

offset = int(''.join(str(x) for x in sequence[:7]))

skip = reversed((sequence * 10000)[offset:])
it = iter(skip)
for i in range(100):
    print(i)
    out = [next(it)]
    for c in it:
        out.append((out[-1]+c)%10)
    it = iter(out)

print(''.join(str(x) for x in seq[:8]))
print(''.join(str(x) for x in itertools.islice(reversed(out), 8)))
