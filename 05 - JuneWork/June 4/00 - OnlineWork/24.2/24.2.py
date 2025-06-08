#0123456789 ABCDEF - 16Ch
s = open(r"00 - OnlineWork\24.2\24_10724.txt").readline()
for i in "QWRTYUIOPSGHJKLZXVNM":
    s = s.replace(i,"-")
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if c[0] != "0" and c.count("-") == 0:
            m = max(m,len(c))
        else:
            break
print(m)

#Answear = 21