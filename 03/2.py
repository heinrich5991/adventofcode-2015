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
pos = [numpy.array([0, 0]), numpy.array([0, 0])]
pos_idx = False
visited = {(0, 0)}
for d in dirs:
    pos[pos_idx] += d
    visited.add((pos[pos_idx][0], pos[pos_idx][1]))
    pos_idx = not pos_idx
print(len(visited))
