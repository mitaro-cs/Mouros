s = open(r"OnlineWork\24.6 min\24_21717.txt").readline()
m = 10000

# Ch 1
for l in range(len(s)):
    for r in range(l+m,l,-1):
        c = s[l:r+1]
        if c.count("RSQ") < 130 :
            break
        elif c.count("RSQ") == 130 and c[-1] != "Q":
            m = min(m,len(c))
print(m)

# Ch 2 not lq
# for l in range(len(s)):
#     for r in range(l,l+m):
#         c = s[l:r+1]
#         if c.count("RSQ") == 130 and c[-1] != "Q":
#             m = min(m,len(c))
#         elif c.count("RSQ") > 130:
#             break
# print(m)