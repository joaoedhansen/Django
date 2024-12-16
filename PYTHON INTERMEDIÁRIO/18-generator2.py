def gen():
    print('COMEÇOU')
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen()

    print('CONTINUOU')
    yield 4
    yield 5
    yield 6

g1 = gen2()

for y in g1:
    print(y)