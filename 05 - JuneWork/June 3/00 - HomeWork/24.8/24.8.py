s = open(r"HomeWork\24.8\24_8_1.txt").readline()
s = s.replace("A","1")
s = s.replace("U","1")
s = s.replace("C","0")
s = s.replace("D","0")
s = s.replace("F","0")
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if len(c) % 2 == 0:
            if all(c[i]+c[i+1] in "01" for i in range(0,len(c),2)):
                m = max(m,len(c))
            else:
                break
print(m//2)

# Answear = 173