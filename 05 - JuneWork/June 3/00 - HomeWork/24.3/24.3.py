s = open(r"HomeWork\24.3\24_3_1.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if "XY" not in c and "XZ" not in c:
            m = max(m,len(c))
        else:
            break
print(m)
#Answer = 25