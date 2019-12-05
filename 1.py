with open('../1.txt') as f:
    i = [int(x) for x in f]

print(sum([x//3-2 for x in i]))

s=0
while i:
    m = i.pop()
    w = m//3-2
    if w > 0:
        s += w
        i.append(w)
print(s)
