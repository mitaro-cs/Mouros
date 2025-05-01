from ipaddress import *

k = 0
for a in range(256):
    net = ip_network(f"207.0.{a}.167/255.255.255.192",0)
    for ad in net:
        res = bin(int(ad))[2:].zfill(32)
        left = res[:16]
        right = res[16:]
        if left.count("0") <= right.count("0"):
            break
    else:
        k += 1
print(k)