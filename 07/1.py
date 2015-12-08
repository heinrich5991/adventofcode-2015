import functools

def evaluate(data, wire):
    @functools.lru_cache(maxsize=None)
    def eval(wire):
        try:
            return int(wire)
        except ValueError:
            pass

        d = data[wire]
        if len(d) == 1:
            operand = d[0]
            result = eval(operand)
        elif len(d) == 2:
            # NOT
            operand = d[1]
            result = ~eval(operand)
        elif len(d) == 3:
            op = d[1]
            operand1 = d[0]
            operand2 = d[2]
            if op == 'AND':
                result = eval(operand1) & eval(operand2)
            elif op == 'OR':
                result = eval(operand1) | eval(operand2)
            elif op == 'LSHIFT':
                result = eval(operand1) << eval(operand2)
            elif op == 'RSHIFT':
                result = eval(operand1) >> eval(operand2)
        return result & ((1 << 16) - 1)

    return eval(wire)

raw = (line.split() for line in open('input'))
wires = {r[-1]: r[:-2] for r in raw}
print(evaluate(wires, "a"))
