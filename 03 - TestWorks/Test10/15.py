for a in range(1,1000):
    if all(((x % 20 == 0) <= (x % 11 != 0)) or (x + a >= 300) for x in range(1,1000) for y in range(1,1000)):
        print(a)
        break
    
        