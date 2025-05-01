def tr(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

for a in range(1,1000):
    if all(not((tr(x,11,18) == (not(max(x,5) > 15))) and tr(x,a,5)) for x in range(1,1000)):
        print(a)
