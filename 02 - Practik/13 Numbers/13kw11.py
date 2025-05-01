from ipaddress import *

for a in range(256):
    net = ip_network(f"217.109.{a}.94/255.255.254.0",0)
    for ad in net:
        res = bin(int(ad))[2:].zfill(32)
        right = res[16:]
        left = res[:16]
        if left.count("0")>right.count("0"):
            break
    else:
        print(a)