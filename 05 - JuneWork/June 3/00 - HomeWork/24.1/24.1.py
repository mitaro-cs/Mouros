s = open(r"HomeWork\24.1\24_1_1.txt").readline()
s = s.replace("A","+")
s = s.replace("E","+")

m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if "++" not in c:
            m = max(m,len(c))
        else:
            break
print(m)

#Answer = 758