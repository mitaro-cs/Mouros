def f7(n):
    s = ""
    while n > 0:
        s += str(n%7)
        n //= 7
    return s[::-1]

max0 = 0
for x in range(1,2031):
    res = f7(7**170 + 7**100 - x)
    if res.count("0") > max0:
        max0 = res.count("0")
print(max0)