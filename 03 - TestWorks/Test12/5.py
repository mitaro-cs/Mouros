for n in range(1,1000):
    num = bin(n)[2:]
    halflen = len(num)//2
    if (num.count("1") + num.count("0")) % 2 == 0:
        num = num[:len(num)//2] + "1" + num[len(num)//2:]
    res = int(num,2)
    if res <= 26:
        print(n)
        
        
    