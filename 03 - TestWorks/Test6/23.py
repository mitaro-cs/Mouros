def f(n,m):
    if n > m or n == 18: return 0 
    if n == m: return 1
    return f(n+1,m) + f(n+4,m) + f(n*2,m)

print(f(4,11) * f(11,28))
