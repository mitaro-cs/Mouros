from ipaddress import *
k = 0
net = ip_network("203.68.128.0/255.255.192.0",0)
for ad in net:
    a = bin(int(ad))[2:].zfill(32)
    if a.count("1") % 7 != 0:
        k += 1
print(k)
