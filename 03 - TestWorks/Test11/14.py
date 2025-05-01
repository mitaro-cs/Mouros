def f9(n):
    s = []
    while n>0:
        s.append(n%9)
        n //= 9
    return s

s = f9(249**540 - 6*9**550 + 21*3*511 - 3*3**70 - 200)
print(s.count(8))