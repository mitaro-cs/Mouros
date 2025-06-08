from ipaddress import *
net = ip_network("211.46.0.0/255.255.128.0",0)
k = 0
for ad in net:
    res = bin(int(ad))[2:].zfill(32)
    if res.count("1") % 4 == 0 and res[-2:] == "11":
        k += 1
print(k)
