from ipaddress import *
net = ip_network("112.208.0.0/255.255.128.0",0)
k = 0
for ad in net:
    a = bin(int(ad))[2:].zfill(32)
    if a.count("1") % 11 == 0:
        k += 1
print(k)