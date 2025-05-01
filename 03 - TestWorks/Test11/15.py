def f(a,b,c):
    return a + b > c and b + c > a and a + c > b

for a in range(1,1000):
    if all(not((f(x,11,18) == (not(max(x,5) > 15))) and f(x,a,5)) for x in range(1,1000) for y in range(1,1000)):
        print(a)
        