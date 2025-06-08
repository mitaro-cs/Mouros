s = open(r"HomeWork\24.5\24_5_1.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if "XZZY" not in c:
            m = max(m,len(c))
        else:
            break
print(m)

#Answer = 1713