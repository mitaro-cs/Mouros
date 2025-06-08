s = open(r"HomeWork\24.7\24_7_1.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if len(c) % 3 == 0:
            if all(c[i] + c[i+1] + c[i+2] in ["NPO","PNO"] for i in range(0,len(c),3)):
                m = max(m,len(c))
            else:
                break
print(m//3)

#Answear = 327