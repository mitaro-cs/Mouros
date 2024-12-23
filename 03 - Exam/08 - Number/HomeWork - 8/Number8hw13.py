from itertools import *
res = set()

for i in permutations("МИТРОФАН",6):
   a = "".join(i)
   if ("ИО" not in a and "ОИ" not in a and "ОА" not in a and "АО" not in a and "ИА" not in a and "АИ" not in a) and\
      (a.count("М") + a.count("Т") + a.count("Р") + a.count("Ф") + a.count("Н")) > (a.count("И") + a.count("А") + a.count("О")):
      res.add(a)
print(len(res))
