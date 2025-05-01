from ipaddress import *
k = 0
net = ip_network("5.2.5.0/255.255.0.0",0)
for ad in net:
    a = bin(int(ad))[2:].zfill(32)
    if a.count("0") % 25 ==0:
        k += 1
print(k)
