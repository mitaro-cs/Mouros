s = open(r"02 - Practik\14 Numbers\14Number5\24_863.txt").readline()

m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if all(c[i]!=c[i+1] for i in range(len(c)-1)):
            m = max(m,len(c))
        else:
            break
print(m)