import itertools

from intcode import intcode_v3, ascii_input, ascii_output

with open('../25.txt') as f:
    instructions = [int(x) for x in f.read().split(',')]

droid = intcode_v3(instructions)

# directions and safe items determined manually.
commands = ['south\n',
            'take astronaut ice cream\n',
            'north\n',
            'east\n',
            'take mouse\n',
            'north\n',
            'take spool of cat6\n',
            'north\n',
            'take hypercube\n',
            'east\n',
            'take sand\n',
            'south\n',
            'take antenna\n',
            'north\n',
            'west\n',
            'south\n',
            'south\n',
            'south\n',
            'take mutex\n',
            'west\n',
            'take boulder\n',
            'south\n',
            'south\n',
            'south\n',
            'west\n',
            'south\n']

items = ['astronaut ice cream',
         'mouse',
         'spool of cat6',
         'hypercube',
         'sand',
         'antenna',
         'mutex',
         'boulder']

output = ''.join(ascii_output(droid))
#print(output, end='')
for command in commands:
    #print(command)
    initial = ascii_input(droid, command)
    output = ''.join(ascii_output(droid, initial))
    #print(output, end='')

for item in items:
    #print(f'drop {item}')
    initial = ascii_input(droid, f'drop {item}\n')
    output = ''.join(ascii_output(droid, initial))
    #print(output, end='')

print('collected all items, at security door')

try:
    oldcombo = ()
    for i in range(len(items)):
        for combo in itertools.combinations(items, i):
            for item in oldcombo:
                if item not in combo:
                    #print(f'drop {item}')
                    initial = ascii_input(droid, f'drop {item}\n')
                    output = ''.join(ascii_output(droid, initial))
                    #print(output, end='')
            print('trying', ', '.join(combo))
            for item in combo:
                if item not in oldcombo:
                    #print(f'take {item}')
                    initial = ascii_input(droid, f'take {item}\n')
                    output = ''.join(ascii_output(droid, initial))
                    #print(output, end='')
            oldcombo = combo
            #print('south')
            initial = ascii_input(droid, 'south\n')
            output = ''.join(ascii_output(droid, initial))
            #print(output, end='')
            if 'heavier' not in output and 'lighter' not in output:
                print(output, end='')
except StopIteration:
    pass
