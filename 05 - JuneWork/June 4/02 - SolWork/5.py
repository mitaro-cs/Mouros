for n in range(1,1000):
    n2 = bin(n)[2:]
    n2 += str(n2.count("1") % 2)
    n2 += str(n2.count("1") % 2)
    res = int(n2,2)
    if res > 253:
        print(n)
        break
    
