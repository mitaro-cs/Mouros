clustersA = [[], [], []]

for line in open(r"02 - Practik\27 Number AnomaliEXT\27A.txt"):
    x, y = [float(i) for i in line.split()]
    if y > 7 or y > 0 and x < -1 or 0 <= x <= 0.5 and -5 <= y <= -2 or y < -6:
        pass
    elif 0 < y < 7 and x > -1:
        clustersA[0].append([x, y])
    elif -6 < y < 0 and x < 0:
        clustersA[1].append([x, y])
    else:
        clustersA[2].append([x, y])


clustersB = [[], [], [], [], []]

for line in open(r"02 - Practik\27 Number AnomaliEXT\27B.txt"):
    x,y = [float(i) for i in line.split()]
    if x < -45 and y > 40 or -20 < x < -15 and y > 40 or -35 < x < -30 and y < 40 or -10 < x < -5 and y < 40:
        pass
    elif y > 40 and -45 < x < -20:
        clustersB[0].append([x,y])
    elif y > 40 and x > -15:
        clustersB[1].append([x,y])
    elif y < 40 and x < -35:
        clustersB[2].append([x,y])
    elif y < 40 and -30 < x < -10:
        clustersB[3].append([x,y])
    else:
        clustersB[4].append([x,y])

def d(a,b):
    x1, y1 = a
    x2, y2 = b
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def edge(cl):
    m = []
    for p in cl:
        sm = sum(d(p,p1) for p1 in cl)
        m.append([sm,p])
    return max(m)[1]

edgesA = [edge(i) for i in clustersA]
edgesB = [edge(i) for i in clustersB]

txa = sum(x for x,y in edgesA) / 3 * 10000
tya = sum(y for x,y in edgesA) / 3 * 10000
txb = sum(x for x,y in edgesB) / 5 * 10000
tyb = sum(y for x,y in edgesB) / 5 * 10000

print(int(txa),int(tya))
print(int(txb),int(tyb))