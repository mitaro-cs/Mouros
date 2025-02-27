def f(x,y):
   if x > y: return 0
   if x == y: return 1
   return f(x+1,y) + f(x+3,y) + f(x*2,y)
print(f(2, 6) * f(6, 10) * f(10, 14))