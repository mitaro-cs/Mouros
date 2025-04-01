def f(n):
    s = ""
    while n > 0:
        s += str(n%4)
        n //= 4
    return s[::-1]


for n in range(1,1000):
    n4 = f(n)
    if n % 4 == 0:
        n4 += n4[-2:]
    else:
        n4 += f((n%4)*2)
    r = int(n4,4)
    if r >= 1025:
        print(n)
        break



