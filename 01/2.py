floor = 0
for pos, c in enumerate(open("input").read()):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    if floor < 0:
        print(pos + 1)
        break
