def f(n,m):
    if n < m: return 0 
    if n == m: return 1
    return f(n-1,m) + f(n//2,m)

print(f(30,12) * f(12,1))
