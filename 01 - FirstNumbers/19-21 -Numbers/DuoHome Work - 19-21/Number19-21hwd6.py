def f(s1,s2,m):
   if s1 + s2 >= 259: return m % 2 == 0
   if m == 0 : return 0
   sm = [f(s1+1,s2,m-1), f(s1,s2+1,m-1), f(s1*2,s2,m-1), f(s1,s2*2,m-1)]
   if m % 2 == 0:
      return all(sm) # вариация 19 "any"
   else:
      return any(sm)
   
#print("19", [s for s in range(1,242) if f(17,s,2)])
print("20", [s for s in range(1,242) if not f(17,s,1) and f(17,s,3)])
print("21", [s for s in range(1,242) if f(17,s,4) and not f(17,s,2)])
