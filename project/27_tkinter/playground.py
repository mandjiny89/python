def add(*args):
    t = 0
    for n in args:
        t += n
    return t

print(add(1,2,3,4,5))