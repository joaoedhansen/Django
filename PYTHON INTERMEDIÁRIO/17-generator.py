def generator(n=0, maximum=10):
    while True:
        yield n

        n += 1

        if n > maximum:
            return #parar ao chegar no máximo

gen = generator()

for n in gen:
    print(n)
