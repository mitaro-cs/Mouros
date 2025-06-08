s = open(r"02 - Practik\14 Numbers\14Number4\24_16333.txt").readline()
for i in "QRW":
    s = s.replace(i,"+")
for i in "124":
    s = s.replace(i,"-")

m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if "++" not in c and "--" not in c:
            m = max(m,len(c)) 
        else:
            break
print(m)