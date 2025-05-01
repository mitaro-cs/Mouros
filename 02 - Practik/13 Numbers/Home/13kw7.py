from ipaddress import *
for a in range(0,256):
    net = ip_network(f"248.112.{a}.35/255.255.255.240",0)
    for ad in net:
        w = bin(int(ad))[2:].zfill(32)
        left = w[:16]
        right = w[16:]
        if left.count("0") > right.count("0"):
            break
    else:
        print(a)
