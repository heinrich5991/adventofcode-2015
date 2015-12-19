import re
NUMBER_RE=re.compile('-?[0-9]+')
print(sum(int(m) for m in NUMBER_RE.findall(open('input').read())))
