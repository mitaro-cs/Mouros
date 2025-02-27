def isprime(n):
    d = 2
    while d**2 <= n:
        if n%d == 0:
            return False
        d += 1
    return True

k = 0
for n in range(2943444, 2943529):
    m = isprime(n)
    if m:
        k += 1
        print(k, n, sep=" - ")
