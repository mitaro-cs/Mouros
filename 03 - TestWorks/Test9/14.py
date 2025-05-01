def f5(n):
    s = ""
    while n>0:
        s += str(n%5)
        n //= 5
    return s[::-1]

s = f5(4 * 25**2022 - 2 * 5**2000 + 125**1011 - 3 + 5**100 - 660)
print(s.count("4"))