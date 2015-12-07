import functools
import operator
prod = lambda i: functools.reduce(operator.mul, i, 1)
    
dims = (tuple([int(x) for x in line.split("x")]) for line in open("input"))
lengths = (2 * (sum(dim) - max(dim)) + prod(dim) for dim in dims)
print(sum(lengths))
