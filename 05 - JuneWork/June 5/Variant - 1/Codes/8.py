from itertools import *
k = 0
for i in product("АВНРЬЯ",repeat=5):
    a = "".join(i)
    print(i, a)
    k += 1
    if a[0] != "Я" and a.count("Ь") <= 1 and "ЯЯ" not in a:
        print(k)