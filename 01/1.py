from collections import Counter
c = Counter(open("input").read())
print(c['('] - c[')'])
