def merge(a, b):
    res = []
    d = a + b
    while d:
        res.append(d.pop(d.index(min(d))))
    return res
