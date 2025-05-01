for n in range(1,1000):
    num = bin(n)[2:]
    if n % 2 == 0:
        num += "0"
    else:
        num += "1"
    if num.count("1") % 3 == 0:
        num = "11" + num[2:]
    else:
        num = "10" + num[2:]
    res = int(num,2)
    if res <= 37:
        print(n)
        break
    