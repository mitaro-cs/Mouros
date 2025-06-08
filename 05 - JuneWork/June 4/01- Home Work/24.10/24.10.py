s = open(r"01- Home Work\24.10\24_10_1.txt").readline()
s = s.replace("X","1")
s = s.replace("Y","2")
s = s.replace("Z","3")
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if all(c[i] <= c[i+1] for i in range(len(c)-1)):
            m = max(m,len(c))
        else:
                break
print(m)