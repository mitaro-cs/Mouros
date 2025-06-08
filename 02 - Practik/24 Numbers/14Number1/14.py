s = open(r"02 - Practik\14 Numbers\14Number1\24_7624.txt").readline()
s = s.replace("Y","X")
s = s.replace("Z","X")

m = 0

for l in range(len(s)):
    for r in range(l+m, len(s)):
        c = s[l:r+1]
        if "XX" not in c:
            m = max(m,len(c))
        else:
            break

print(m)