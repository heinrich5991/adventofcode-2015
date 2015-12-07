import hashlib
import itertools
def do(prefix):
    for i in itertools.count(start=1):
        if hashlib.md5((prefix + str(i)).encode()).hexdigest().startswith("0" * 6):
            return i
print(do("bgvyzdsv"))
