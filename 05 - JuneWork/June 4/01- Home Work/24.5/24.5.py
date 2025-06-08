s = open(r"01- Home Work\24.5\24_5_1.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        if "DD" in c and "FE" not in c:
            break
        elif "FE" in c:
            m = max(m,len(c))
print(m)