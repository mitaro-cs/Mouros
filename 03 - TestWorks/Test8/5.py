def f4(n):
    s = ""
    while n > 0:
        s += str(n%4)
        n //= 4
    return s[::-1]

for n in range(1,1000):
    num = f4(n)
    if n % 4 == 0:
        num += num[-2:]
    else:
        num += f4((n%4)*2)
    res = int(num,4)
    if res >= 1088:
        print(n)
        break
    