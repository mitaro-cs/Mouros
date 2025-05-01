# Mask = 255.255.a.0
#  Ip  = 255.211.33.100
from ipaddress import *
for a in range(16,25):
    net = ip_network(f"255.211.33.100/{a}",0)
    for ad in net:
        res = bin(int(ad))[2:].zfill(32)
        left = res[:16]
        right = res[16:]
        if left.count("1") < right.count("1"):
            break
    else:
        print(net.netmask)