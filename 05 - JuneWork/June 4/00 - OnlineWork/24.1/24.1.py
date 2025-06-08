s = open(r"00 - OnlineWork\24.1\24_1144.txt").readline()
m = 10000
for l in range(len(s)):
    for r in range(l+2,l+m):
        c = s[l:r+1]
        if c[0] != "A":
            break
        elif c[0] == "A" and c[-1] == "F":
            m = min(m,len(c))
print(m)
        
#Answear = 7