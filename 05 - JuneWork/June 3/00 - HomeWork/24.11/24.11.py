s = open(r"HomeWork\24.11\24_11_1.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if c.count("A") <= 1:
            m = max(m,len(c))
        else:
            break
print(m)

#Answear = 337