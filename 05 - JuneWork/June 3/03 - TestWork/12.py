s = "5" + "4"*57
while "5454" in s or "554" in s or "444" in s:
    if "5454" in s:
        s = s.replace("5454","2",1)
    else:
        s = s.replace("554","45",1)
    s = s.replace("444","54",1)

print(s)
