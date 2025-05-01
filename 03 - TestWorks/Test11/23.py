def f(n,m):
    if n < m or n == 10: return 0 # мне кажется где то тут ошибка
    if n == m: return 1
    return f(n-1,m) + f(n//2,m)

print(f(50,20) * f(20,1))
