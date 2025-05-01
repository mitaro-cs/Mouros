from ipaddress import *
for a in range(16,25):
    net = ip_network(f"99.8.254.232/{a}",0)
    for ad in net:
        w = bin(int(ad))[2:].zfill(32)
        left = w[:16]
        right = w[16:]
        if left.count("1") > right.count("1"):
            break
    else:
        print(net.netmask)
        break

