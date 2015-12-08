import ast
string_literals = (line[:-1] for line in open('input'))
print(sum(len(lit) - len(ast.literal_eval(lit)) for lit in string_literals))
