clustersA = [[] ,[]]

for line in open(r"27 Number Anomali\27A_18626.txt"):
    line = line.replace(",",".")
    x,y = [float(i) for i in line.split()]
    if y < 0 and x < 2 or y > 7 and x > 5 :
        pass # ничего не делает (pass отсутствие действия) 
    elif y < 3 and x < 5 or x < 2 or y > 6 and x < 3:
        clustersA[0].append([x,y])
    else:
        clustersA[1].append([x,y])


clustersB = [[], [], []]

for line in open (r"27 Number Anomali\27B_18626.txt"):
    line = line.replace(",",".")
    x,y = [float(i) for i in line.split()]
    if y < 2 and x < 2 or y > 9 and x > 9 or 4 <= y <= 6 and 7 <= x <= 8:
        pass
    elif x < 4:
        clustersB[0].append([x,y])
    elif y > 2 and 4 <= x < 7 or y > x > 4:
        clustersB[1].append([x,y])
    else:
        clustersB[2].append([x,y])

def d(A,B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def center(cl):
    m = []
    for p in cl:
        sm = sum(d(p,p1) for p1 in cl)
        m.append([sm,p])
    return min(m)[1]

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

pxa = sum(x for x,y in centersA) / 2 * 100000
pya = sum(y for x,y in centersA) / 2 * 100000
pxb = sum(x for x,y in centersB) / 3 * 100000
pyb = sum(y for x,y in centersB) / 3 * 100000

print(int(pxa), int(pya))
print("------------")
print(int(pxb), int(pyb))




