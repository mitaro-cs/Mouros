clustersA = [[], []]
for line in open(r"03 - TestWorks\Test12\27var12A.txt"):
    x, y = [float(i) for i in line.split()]
    if y > 15 :
        clustersA[0].append([x,y])
    else:
        clustersA[1].append([x,y])


clustersB = [[], [], []]
for line in open(r"03 - TestWorks\Test12\27var12B.txt"):
    x,y = [float(i) for i in line.split()]
    if x > 0:
        clustersB[0].append([x,y])
    elif y > 0 :
        clustersB[1].append([x,y])
    else:
        clustersB[2].append([x,y])


def d(a,b):
    x1,y1 = a
    x2,y2 = b
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def center(cl):
    m = []
    for p in cl:
        sm = sum(d(p,p1) for p1 in cl)
        m.append([sm,p])
    return min(m)[1]

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

pxa = abs(sum(x for x,y in centersA) / 2 * 10000)
pya = abs(sum(y for x,y in centersA) / 2 * 10000)
pxb = abs(sum(x for x,y in centersB) / 3 * 10000)
pyb = abs(sum(y for x,y in centersB) / 3 * 10000)

print(int(pxa),int(pya))
print(int(pxb),int(pyb))