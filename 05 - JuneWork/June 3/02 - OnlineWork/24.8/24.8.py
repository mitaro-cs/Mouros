s = open(r"OnlineWork\24.8\24_9753.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if c.count("Y") <= 150:
            m = max(m,len(c))
        else:
            break
print(m)

#Answear 244