s = open(r"HomeWork\24.10\24_10_1.txt").readline()
s = s.replace("N","1")
s = s.replace("O","1")
s = s.replace("P","1")
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if "11" not in c:
            m = max(m,len(c))
        else:
            break
print(m)

#Answear = 57