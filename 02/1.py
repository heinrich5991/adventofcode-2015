dims = (tuple([int(x) for x in line.split("x")]) for line in open("input"))
areas = ((x * y, y * z, z * x) for x, y, z in dims)
print(sum(2 * sum(a) + min(a) for a in areas))
