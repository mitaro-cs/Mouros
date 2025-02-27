def isprime(n):
    d = 2
    while d**2 <= n:
        if n%d == 0:
            return False
        d += 1
    return True

def maxd(n):
    d = 2
    while d**2 <= n:
        if n%d == 0:
            if isprime(n//d):
                return 0
            else:
                return n//d
        d += 1
    return 0

k = 0
for n in range(450000+1, 10**10):
    m = maxd(n)
    if m != 0:
        k += 1 
        print(n,m)
        if k == 6:
            break

