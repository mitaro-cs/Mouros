def f11(n):
    s = []
    while n>0:
        s.append(n%11)
        n //= 11
    return s

s = f11(1331**650 - 55*121**610 + 77*11*510 - 3*11**100 - 201)
print(s.count()) 