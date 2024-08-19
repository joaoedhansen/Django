def soma(a, b, c=None):
    if c is not None:
        print(f'{a=} {b=} {c=}', a + b + c)
    else:
        print(f'{a=} {b=}', a + b)

soma(1, 3, 5)
soma(1, 3)