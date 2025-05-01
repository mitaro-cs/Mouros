from ipaddress import *
net = ip_network("252.67.33.87/255.252.0.0",0)
k = 0
for ad in net:
    a = bin(int(ad))[2:].zfill(32)
    right = a[16:] 
    left = a[:16]
    if right.count("1") > left.count("1") * 2:
        k += 1
print(k)  
