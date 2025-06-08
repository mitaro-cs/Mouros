clustersA = [[], [], []]
for line in open(r"03 - TestWork\Files\27_А.txt"):
    x, y = [float(i) for i in line.split()]
    if y > 9 :
        clustersA[0].append([x,y])
    if y < 9 and x < 5 :   
        clustersA[1].append([x,y])
    else:
        clustersA[2].append([x,y])


clustersB = [[], [], [], [], []]
for line in open(r"03 - TestWork\Files\27_Б.txt"):
    x,y = [float(i) for i in line.split()]
    if y > 17:
        clustersB[0].append([x,y])
    if 9 < y < 17 and x < 10:
        clustersB[1].append([x,y])
    if 7 < y < 13 and x > 10:
        clustersB[2].append([x,y])
    if y < 6 and x < 6:
        clustersB[3].append([x,y])
    else:
        clustersB[4].append([x,y])
    
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

pxa = abs(sum(x for x,y in centersA) / 3 * 10000)
pya = abs(sum(y for x,y in centersA) / 3 * 10000)
pxb = abs(sum(x for x,y in centersB) / 5 * 10000)
pyb = abs(sum(y for x,y in centersB) / 5 * 10000)

print(int(pxa),int(pya))
print(int(pxb),int(pyb))