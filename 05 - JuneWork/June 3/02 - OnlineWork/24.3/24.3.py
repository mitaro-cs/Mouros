s = open(r"OnlineWork\24.3\24_3020.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if len(c) % 2 == 0:
            if all(c[i]+c[i+1] in ["ZX","ZY"] for i in range(0,len(c),2)):
                m = max(m,len(c))
            else:
                break
print(m//2)

#Answear = 177