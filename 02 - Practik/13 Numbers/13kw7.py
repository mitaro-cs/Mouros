from ipaddress import *
net = ip_network("157.180.63.114/255.255.255.248",0)
k = 0
for ad in net:
    a = bin(int(ad))[2:].zfill(32)
    if a.count("1") % 4 != 0:
        k += 1 
print(k)