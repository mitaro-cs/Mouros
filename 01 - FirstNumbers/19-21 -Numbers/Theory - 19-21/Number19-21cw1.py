def f(n,m):
   if n >= 435: return m%2 == 0
   if m == 0: return 0
   nn = [f(n+5,m-1),f(n*3,m-1)]
   if m % 2 == 0: 
      return all(nn)
   else:
      return any(nn)
   
print("19", [n for n in range(1, 435) if f(n,2)])
print("20", [n for n in range(1, 435) if not f(n,1) and f(n,3)])
print("21", [n for n in range(1, 435) if f(n,4) and not f(n,2)])

