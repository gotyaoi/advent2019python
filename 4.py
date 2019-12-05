import itertools

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

count = 0
for i in range(246515, 739106):
    s = str(i)
    double = False
    for a, b in pairwise(s):
        if a == b:
            double = True
        elif b < a:
            break
    else:
        if double:
            count += 1

print(count)

#688899
count = 0
for i in range(246515, 739106):
    s = str(i)
    double = False
    in_run = False
    too_long = False
    for a, b in pairwise(s):
        if a == b:
            if not (double or too_long):
                if in_run:
                    too_long = True
                else:
                    in_run = True
        elif b < a:
            break
        else:
            if in_run and not too_long:
                double = True
            in_run = False
            too_long = False
    else:
        if double or (in_run and not too_long):
            count += 1

print(count)
