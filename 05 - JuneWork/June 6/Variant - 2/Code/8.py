from itertools import *
k = 0
for i in product("КОСУФ",repeat=5):
    a = "".join(i)
    k += 1
    if a.count("Ф") == 0 and a.count("У") == 2:
        print(k,a)
