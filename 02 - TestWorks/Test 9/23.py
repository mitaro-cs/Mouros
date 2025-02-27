def f(n,m):
   if n > m: return 0
   if n == m: return 1
   return f(n+1, m) + f(n*2, m) + f(n*3, m)
print(f(3,9) * f(9,30))
