from ipaddress import *
net = ip_network("253.112.169.12/255.255.254.0",0)
k = 0
for ad in net:
    a = bin(int(ad))[2:].zfill(32)
    left = a[:16]
    right = a[16:]
    if right.count("1") >= left.count("1"):
        k += 1 
print(k)