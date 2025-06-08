s = open(r"02 - Practik\14 Numbers\14Number6\24_5551.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if all(c[i] != c[i+1] and c[i]==c[i+2] and c[i+1]==c[i+3]  for i in range(len(c)-3)):
            m = max(m,len(c))
        else:
            break
print(m)
