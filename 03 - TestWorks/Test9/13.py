# Mask = 1111 1111.1111 1100 .0000 0000.0000 0000
#  Ip  = 1111 1100.0100 0011 .0010 0001.0101 0111

a = []
for i in range(2**16):
    s = bin(i)[2:]
    if s.count("1") >= 18:
        a.append(s)
print(len(a))