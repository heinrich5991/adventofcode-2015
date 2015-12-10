import functools
def next_impl(string):
    iter_ = iter(string)
    cur = next(iter_)
    count = 1
    for c in iter_:
        if cur != c:
            yield "{}{}".format(count, cur)
            cur = c
            count = 1
        else:
            count += 1

def next_(string):
    return "".join(next_impl(string))

INPUT = "1113122113"
print(len(list(functools.reduce(lambda x, _: next_(x), range(40), INPUT))))
