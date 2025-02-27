def f(s,m):
   if s >= 40: return m%2 == 0
   if m == 0: return 0
   sm = [f(s+1,m-1), f(s+4,m-1), f(s*2,m-1)]
   if m % 2 == 0:
      return all(sm)
   else:
      return any(sm)

print("19", [s for s in range(1, 39) if f(s,2)])
print("20", [s for s in range(1, 39) if not f(s,1) and f(s,3)])
print("21", [s for s in range(1, 39) if f(s,4) and not f(s,2)])