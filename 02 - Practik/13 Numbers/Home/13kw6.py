from ipaddress import *
for a in range(0,256):
    net = ip_network(f"223.167.{a}.67/255.255.255.192",0)
    for ad in net:
        w = bin(int(ad))[2:].zfill(32)
        right = w[16:] 
        left = w[:16]
        if left.count("0") > right.count("0"):
            break
    else:
        print(a)
        