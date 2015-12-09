import itertools
def pairs(iterable):
    iterable = iter(iterable)
    prev = next(iterable)
    for elem in iterable:
        yield (prev, elem)
        prev = elem

tokens = (line.split() for line in open('input'))
city_pairs = [(t[0], t[2], int(t[4])) for t in tokens]
distances = {}
distances.update({(a, b): distance for a, b, distance in city_pairs})
distances.update({(b, a): distance for a, b, distance in city_pairs})
cities = set()
cities.update({a for a, b, distance in city_pairs})
cities.update({b for a, b, distance in city_pairs})
print(min(sum(distances[(x, y)] for x, y in pairs(path)) for path in itertools.permutations(cities)))
