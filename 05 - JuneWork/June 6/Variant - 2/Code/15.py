def dl(n,m):
    if n % m == 0:
        return True
    else:
        return False
for a in range(1,1000):
    if all((dl(x,a) or ((x == b) <= (not(dl(x,22)))))   for x in range(1,1000) for b in range(60,81)):
        print(a)