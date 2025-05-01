def f8(n):
    s = ""
    while n>0:
        s += str(n%8)
        n //= 8
    return s[::-1]

s = f8(4**2022 - 6 * 4**522 + 5 * 54**510 - 3 * 2**330 - 100)
print(s.count("7"))