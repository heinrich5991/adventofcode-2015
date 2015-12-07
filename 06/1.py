import functools
import numpy
DIM=1000

def do(state, instr):
    point = lambda s: tuple(int(x) for x in s.split(','))
    instr = instr.split()
    cmd = " ".join(instr[:-3])

    start = point(instr[-3])
    end = point(instr[-1])

    if cmd == 'toggle':
        state[start[0]:end[0], start[1]:end[1]] ^= True
    elif cmd == 'turn on':
        state[start[0]:end[0], start[1]:end[1]] = True
    elif cmd == 'turn off':
        state[start[0]:end[0], start[1]:end[1]] = False

    return state

print(functools.reduce(do, open('input'), numpy.array([[False] * DIM] * DIM)).sum())
