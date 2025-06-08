s = open(r"").readline()
m = 10000
for l in range(len(s)):
    for r in range(l+m,l,-1):
        c = s[l:r+1]
        if c.count("Z") >= 120:
            m = min(m,len(c))
        else:
            break
print(m)
