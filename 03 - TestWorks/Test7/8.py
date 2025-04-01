from itertools import *
lf = set()
k = 0
for i in product("АГИЛМНОФ",repeat=5):
    a = "".join(i)
    k += 1
    if a[0] != "Н" and a.count("О") <= 1 and k % 2 != 0:
        lf.add(a)
print(len(lf))
