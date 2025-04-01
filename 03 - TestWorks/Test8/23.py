def f(n,m):
    if n > m or n == 21: return 0 
    if n == m: return 1
    return f(n+2,m) + f(n+3,m) + f(n*5,m)

print(f(1,6) * f(6,35))
