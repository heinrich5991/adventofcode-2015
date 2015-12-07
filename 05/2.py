from collections import Counter
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

def first_req(string):
    def valid_pair(p):
        if c[p] > 2:
            return True
        if c[p] == 2 and p[0] != p[1]:
            return True
        if c[p] == 2 and string.find(p[0] * 3) == -1:
            return True
        return False

    c = Counter(pairs(string))
    return any(valid_pair(p) for p in c)

def second_req(string):
    return any(x == z for x, _, z in triples(string))

print(sum(first_req(s) and second_req(s) for s in open('input')))
