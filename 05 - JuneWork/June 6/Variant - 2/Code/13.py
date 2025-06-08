from ipaddress import *
k = 0
net = ip_network("172.16.192.0/255.255.192.0",0)
for ad in net:
    res = bin(int(ad))[2:].zfill(32)
    if res.count("1") % 5 != 0:
        print(res)
        k += 1 
print(k)
