from itertools import *

chet = 'ACBD'
nechet = '13579'

def f(s):
    for i in range(len(s) - 1):
        if s[i] in chet and s[i + 1] in nechet or s[i] in nechet and s[i + 1] in chet:
            return False
    return True

res = set()
for i in product("0123456789ABCD",repeat = 5):
   a = "".join(i)
   if f(i) and a[0] != '0':
      res.add(a)
print(len(res))
