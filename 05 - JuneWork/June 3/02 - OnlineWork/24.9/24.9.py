s = open(r"OnlineWork\24.9\24_6734.txt").readline()
m = 10000
for l in range(len(s)):
    for r in range(l,l+m):
        c = s[l:r+1]
        if c.count(".") == 7:
            m = min(m,len(c))
            break
print(m)    

#Answear = 16