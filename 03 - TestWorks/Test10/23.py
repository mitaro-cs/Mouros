def f(n,m):
    if n > m or n == 21: return 0 
    if n == m: return 1
    return f(n-1,m) + f(n//2,m)

print(f(60,10) * f(10,2))
