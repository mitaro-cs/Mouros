s = open(r"00 - OnlineWork\24.3\24_21421.txt").readline()
for i in "QWERTYUIOPSDFGHJKLZXCVNM":
    s = s.replace(i,"-")

m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if c[0] != "0" and "-" not in c:
            if c[-1] in "02468A":
                m = max(m,len(c))
        else:
            break
print(m)
#Answear = 19
