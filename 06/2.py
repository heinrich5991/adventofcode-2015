import functools
import numpy
DIM=1000

def do(state, instr):
    point = lambda s: tuple(int(x) for x in s.split(','))
    instr = instr.split()
    cmd = " ".join(instr[:-3])

    start = point(instr[-3])
    end_inclusive = point(instr[-1])
    end = (end_inclusive[0] + 1, end_inclusive[1] + 1)

    if cmd == 'toggle':
        state[start[0]:end[0], start[1]:end[1]] += 2
    elif cmd == 'turn on':
        state[start[0]:end[0], start[1]:end[1]] += 1
    elif cmd == 'turn off':
        state[start[0]:end[0], start[1]:end[1]] -= 1

    return state

print(functools.reduce(do, open('input'), numpy.array([[0] * DIM] * DIM)).sum())
