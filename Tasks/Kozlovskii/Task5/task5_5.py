lst = input('Enter:')
def ranges(lst):
    b = lst.split(' ')
    c = [int(i) for i in b]
    s = e = None
    for i in sorted(c):
        if s is None:
            s = e = i
        elif i == e or i == e + 1:
            e = i
        else:
            yield (s, e)
            s = e = i
    if s is not None:
        yield (s, e)

print(repr(','.join(['%d' % s if s == e else '%d-%d' % (s, e) for (s, e) in ranges(lst)])))




