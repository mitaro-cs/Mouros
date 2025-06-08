from itertools import *
chet = '02468'
nechet = '13579'

def f(s):
    for i in range(len(s) - 1):
        if s[i] in chet and s[i + 1] in nechet or s[i] in nechet and s[i + 1] in chet:
            return False
    return True

res = set()
for i in permutations("0123456789",4):
   a = "".join(i)
   if f(i) and a[0] != '0':
      res.add(a)
print(len(res))
