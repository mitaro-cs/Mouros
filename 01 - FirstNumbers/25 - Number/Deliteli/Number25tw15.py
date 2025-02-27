def isprime(n):
    d = 2
    while d**2<=n:
        if n % d == 0:
            return False
        d += 1
    return True

def sumprime(n):
    d = 2
    sumd = 0
    while d**2 < n:
        if n % d == 0:
            if isprime(d):
                sumd += d
            if isprime(n//d):
                sumd += n//d
        d += 1
    if d**2 == n:
        if isprime(d**2):
            sumd += d
    return sumd

k = 0
for n in range(550000+1, 10**10):
    m = sumprime(n)
    if m % 10 == 1:
        k += 1
        print(n,m, sep=" - ")
        if k == 5:
            break
    

