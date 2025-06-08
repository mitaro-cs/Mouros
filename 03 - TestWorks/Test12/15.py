def f(a,b,c):
    return a + b > c and b + c > a and a + c > b

for a in range(1,1000):
    if all(not((f(x,12,20) == (not(max(x,5) > 28))) and f(x,a,3)) for x in range(1,1000) for y in range(1,1000)):
        print(a)
        