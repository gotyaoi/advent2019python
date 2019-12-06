with open('../6.txt') as f:
    orbits = dict(reversed(x[:-1].split(')')) for x in f)

count = 0
for body, parent in orbits.items():
    count += 1
    while parent != 'COM':
        count += 1
        parent = orbits[parent]

print(count)

parent = orbits['SAN']
san_line = [parent]
while parent != 'COM':
    parent = orbits[parent]
    san_line.append(parent)

parent = orbits['YOU']
you_line = [parent]
while parent != 'COM':
    parent = orbits[parent]
    you_line.append(parent)

for san, you in zip(reversed(san_line), reversed(you_line)):
    if san == you:
        common = san_line.pop()
        you_line.pop()
    else:
        break

count = 0
parent = orbits['SAN']
while parent != common:
    count += 1
    parent = orbits[parent]

parent = orbits['YOU']
while parent != common:
    count += 1
    parent = orbits[parent]

print(count)
