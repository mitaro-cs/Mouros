s = "5" * 54 + "7"
while "722" in s or "557" in s:
   if "722" in s:
      s = s.replace("722","57",1)
   else:
      s = s.replace("557","72",1)
print(s)