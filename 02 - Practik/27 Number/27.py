clustersA = [[], [], []]
for line in open(r"27 Number\27A.txt"):
    line = line.replace(",",".")
    x, y = [float(i) for i in line.split()]
    if y < 5 :
        clustersA[0].append([x,y])
    elif x < 5:
        clustersA[1].append([x,y])
    else:
        clustersA[2].append([x,y])

clustersB = [[], [], [], [], []]
for line in open(r"27 Number\27B.txt"):
    x,y = [float(i) for i in line.split()]
    if y < 10 and y > x:
        clustersB[0].append([x,y])
    if x < 10 and y < x:
        clustersB[1].append([x,y])
    if y < 10 and x > 10:
        clustersB[2].append([x,y])
    if y > 10 and y < x:
        clustersB[3].append([x,y]) 
    if x > 10 and y > x:
        clustersB[4].append([x,y])

def d(a,b):
    x1,y1 = a
    x2,y2 = b
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def center(cl):
    m = [] # min element 
    for p in cl:
        sm = sum(d(p,p1) for p1 in cl)
        m.append([sm,p])
    return min(m)[1]

centersA = [ center(cl) for cl in clustersA]
centersB = [ center(cl) for cl in clustersB]

pxa = sum(x for x,y in centersA) / 3 * 100000
pya = sum(y for x,y in centersA) / 3 * 100000
pxb = sum(x for x,y in centersB) / 5 * 100000
pyb = sum(y for x,y in centersB) / 5 * 100000     

print(int(pxa),int(pya))
print(int(pxb),int(pyb))