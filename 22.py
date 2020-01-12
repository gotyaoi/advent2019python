def parse(line):
    if line.startswith('deal into'):
        return (-1, -1) # -x - 1
    elif line.startswith('cut'):
        return (1, -int(line[4:])) # x - n
    elif line.startswith('deal with'):
        return (int(line[20:]), 0) # nx + 0

with open('../22.txt') as f:
    operations = [parse(l) for l in f]

def linearize(mod):
    # start with 1x + 0
    multiplier = 1
    adder = 0
    for m, a in operations:
        # next(current(x)), so next_multiplier(multiplier*x + adder) + next_adder
        # next_multiplier*multiplier*x + next_multiplier*adder + next_adder
        multiplier = (multiplier * m) % mod
        adder = (adder * m + a) % mod
    return multiplier, adder

multiplier, adder = linearize(10007)
print((2019 * multiplier + adder) % 10007)

# keep going
# one = mx+a
# two = m(mx+a)+a
# two = m**2x+ma+a
# two = m**2x+a*(m+1)
# thr = m(m**2x+ma+a)+a
# thr = m**3x+m**2a+ma+a
# thr = m**3x+a*(m**2+m+1)
# nth_m = m**n
# nth_a = a*(m**(n-1)+m**(n-2)+...+m+1)
# sum of consecutive powers
# nth_a = a*(m**n-1)//(m-1)

multiplier, adder = linearize(119315717514047)

# use Euler's theorem to get the modular multiplicative inverse.
# only works because the chosen deck size and number of shuffles are coprime.
def inverse(n, mod):
    return pow(n, mod-2, mod)

multiplier, adder = (pow(multiplier, 101741582076661, 119315717514047),
                     (adder*(pow(multiplier, 101741582076661, 119315717514047)-1)*inverse(multiplier-1, 119315717514047))%119315717514047)

# where does 2020 go. incorrect.
#print((2020 * multiplier + adder) % 119315717514047)

# 2020 = x * multiplier + adder
# 2020 - adder = x * multiplier
# x = 2020 - adder / multiplier
print(((2020-adder)*inverse(multiplier, 119315717514047))%119315717514047)
