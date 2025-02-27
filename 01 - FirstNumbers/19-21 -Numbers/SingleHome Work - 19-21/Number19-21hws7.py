def f(n,m):
   if n >= 21: return m%2 == 0
   if m == 0: return 0
   nn = [f(n+1,m-1),f(n+2,m-1),f(n*2,m-1)]
   if m % 2 == 0: 
      return all(nn) # Не меняеться 19
   else: 
      return any(nn)
   
print("19", [n for n in range(1, 21) if f(n,3)])
print("20", [n for n in range(1, 21) if not f(n,1) and not f(n,3) and f(n,5)])
print("21", [n for n in range(1, 21) if f(n,5) and not f(n,1) and not f(n,3)])

