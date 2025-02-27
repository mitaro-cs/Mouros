from itertools import *
res = set()

for i in product("АРМИЯЖДЁТ",repeat=7):
   a = "".join(i)
   if ("АР"or"АМ"or"АЖ"or"АД"or"АТ"or"ИР"or"ИМ"or"ИЖ"or"ИД"or"ИТ"or"ЯР"or"ЯМ"or"ЯЖ"or"ЯД"or"ЯТ"or"ЁР"or"ЁМ"or"ЁЖ"or"ЁД"or"ЁТ") not in a:
      res.add(a)
print(len(res))
