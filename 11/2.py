import string

def pairs(iterable):
    iterable = iter(iterable)
    prev = next(iterable)
    for elem in iterable:
        yield (prev, elem)
        prev = elem

def triples(iterable):
    iterable = iter(iterable)
    prevs = (next(iterable), next(iterable))
    for elem in iterable:
        yield prevs + (elem,)
        prevs = (prevs[1], elem)

def increase(l):
    max = len(SOURCE)
    for i in range(len(l), 0, -1):
        i -= 1
        l[i] += 1
        if l[i] >= max:
            l[i] %= max
        else:
            break
    return l

def to_list(input):
    return [SOURCE.index(c) for c in input]

def to_string(l):
    return "".join(SOURCE[i] for i in l)

def condition1(l):
    return any(a + 2 == b + 1 == c for a, b, c in triples(l))

def condition2(l):
    return all(a not in [SOURCE.index(c) for c in "iol"] for a in l)

def condition3(l):
    return sum(a == b for a, b in pairs(l)) \
           - any(a == b == c for a, b, c in triples(l)) >= 2

SOURCE="abcdefghijklmnopqrstuvwxyz"
INPUT="cqjxjnds"

l = to_list(INPUT)
while True:
    if condition1(l) and condition2(l) and condition3(l):
        break
    l = increase(l)
l = increase(l)
while True:
    if condition1(l) and condition2(l) and condition3(l):
        print(to_string(l))
        break
    l = increase(l)
