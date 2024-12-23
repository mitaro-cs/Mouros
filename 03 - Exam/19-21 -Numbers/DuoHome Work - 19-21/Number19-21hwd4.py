def f(s1,s2,m):
   if s1 + s2 >= 263: return m % 2 == 0
   if m == 0 : return 0
   sm = [f(s1+1,s2,m-1), f(s1,s2+1,m-1),  f(s1*2,s2,m-1), f(s1,s2*2,m-1)]
   if m % 2 == 0:
      return all(sm) # вариация 19 "any"
   else:
      return any(sm)
   
#print("19", [s for s in range(1,246) if f(17,s,2)])
print("20", [s for s in range(1,246) if not f(s,17,1) and f(s,17,3)])
print("21", [s for s in range(1,246) if f(s,17,4) and not f(s,17,2)])
