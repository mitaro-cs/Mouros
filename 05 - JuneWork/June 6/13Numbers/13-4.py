from ipaddress import *
net = ip_network("203.68.128.0/255.255.192.0",0)
k = 0
for ad in net:
    res = bin(int(ad))[2:].zfill(32)
    if res.count("1") % 7 != 0:
        k += 1

print(k)