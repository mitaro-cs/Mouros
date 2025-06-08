s = open(r"OnlineWork\24.7\24_20909.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if c.count("AB") == 100:
            m = max(m,len(c))
        elif c.count("AB") > 100:
            break
print(m)
        
# Answear = 750
