def f(s1,s2,m):
   if s1 + s2 >= 123: return m % 2 == 0
   if m == 0 : return 0
   sm = [f(s1+1,s2,m-1), f(s1,s2+1,m-1), f(s1*2,s2,m-1), f(s1,s2*2,m-1)]
   if m % 2 == 0:
      return all(sm)
   else:
      return any(sm)

#print("19", [s for s in range(1,114) if f(10,s,2)]) #присутвует неудачный ход
print("20", [s for s in range(1,114) if not f(10,s,1) and f(10,s,3)])
print("21", [s for s in range(1,114) if f(10,s,4) and not f(10,s,2)])
