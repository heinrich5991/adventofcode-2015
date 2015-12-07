import functools
import numpy
prod = lambda i: functools.reduce(operator.mul, i, 1)
    
DIRS={
    '^': numpy.array([ 0,  1]),
    '>': numpy.array([ 1,  0]),
    'v': numpy.array([ 0, -1]),
    '<': numpy.array([-1,  0]),
}
dirs = (DIRS[c] for c in open("input").read() if c in DIRS)
pos = numpy.array([0, 0])
visited = {(pos[0], pos[1])}
for d in dirs:
    pos += d
    visited.add((pos[0], pos[1]))
print(len(visited))
