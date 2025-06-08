s = open(r"01- Home Work\24.1\24_1_1.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if "A" not in c and "E" not in c:
            m = max(m,len(c))
        else:
            break
print(m)