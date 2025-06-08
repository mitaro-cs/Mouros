s = open(r"01- Home Work\24.11\24_11_1.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if all(c[i] == c[i+1] == c[i+2]for i in range(len(c)-2)):
            break
        else:
            m = max(m,len(c))
print(m)
