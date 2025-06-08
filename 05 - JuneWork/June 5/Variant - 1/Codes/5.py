res = []
def f3(n):
    s = ""
    while n > 0:
        s += str(n%3)
        n //= 3
    return s[::-1]

for n in range(1,1000):
    n3 = f3(n)
    if n % 3 == 0:
        n3 += n3[-2:]
    else:
        n3 += f3(n3.count("1") + 2*n3.count("2"))
    r = int(n3,3)
    if r % 2 == 0 and r > 220:
        res.append(r)
        
print(min(res))