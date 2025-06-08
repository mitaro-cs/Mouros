from functools import *
@lru_cache(None)

def f(n):
    if n <= 1000:
        return n**(n**2)
    else:
        return n + 2*f(n-2) + 6*f(n-6)
    
for i in range(30000):
    f(i)

print(f(20024) - 2*f(20022) - 3*f(20020) + 18*f(20014))