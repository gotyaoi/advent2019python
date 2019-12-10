from itertools import zip_longest
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

with open('../8.txt') as f:
    layers = list(grouper(f.read()[:-1], 150))

best = 151
best_layer = layers[0]
for layer in layers:
    zeroes = layer.count('0')
    if zeroes < best:
        best = zeroes
        best_layer = layer

print(best_layer.count('1') * best_layer.count('2'))

output = []
for column in zip(*layers):
    for c in column:
        if c == '0':
            output.append(' ')
            break
        elif c == '1':
            output.append('\u2588')
            break

for line in grouper(output, 25):
    print(''.join(line))
