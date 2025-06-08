def f(n,m):
    if n < m or n == 4: return 0
    if n == m: return 1
    return f(n-1,m) + f(n//2,m)

print(f(60,20) * f(20,1))
