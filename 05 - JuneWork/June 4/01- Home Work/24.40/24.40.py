s = open(r"").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if:
            m = max(m,len(c))
        else:
            break
print(m)