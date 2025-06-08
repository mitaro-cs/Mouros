s = open(r"01- Home Work\24.9\24_9_1.txt").readline()
s = s.replace("A","-")
s = s.replace("B","-")
s = s.replace("C","-")
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if "-" in c:
            break
        elif all(c[i] <= c[i+1] for i in range(len(c)-1)):
            m = max(m,len(c))
print(m)