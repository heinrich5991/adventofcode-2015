strings = (line[:-1] for line in open('input'))
print(sum(2 + s.count('\\') + s.count('\"') for s in strings))
