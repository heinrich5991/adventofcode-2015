from collections import Counter
def pairs(iterable):
    iterable = iter(iterable)
    prev = next(iterable)
    for elem in iterable:
        yield (prev, elem)
        prev = elem

def first_req(string):
    c = Counter(string)
    return sum(c[v] for v in "aeiou") >= 3

def second_req(string):
    return any(x == y for x, y in pairs(string))

def third_req(string):
    return all(p not in ["ab", "cd", "pq", "xy"] for p in pairs(string))

print(sum(first_req(s) and second_req(s) and third_req(s) for s in open('input')))
