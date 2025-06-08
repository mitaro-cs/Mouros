s = open(r"OnlineWork\24.5\24_13100.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]    
        if c.count("C") <= 2 and c.count("D") <= 2 :
            m = max(m,len(c))
        else:
            break
print(m)

#Answear = 253