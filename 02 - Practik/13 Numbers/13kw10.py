from ipaddress import * 
net = ip_network("172.18.200.14/255.255.0.0",0)

k = 0
for ad in net:
    res = bin(int(ad))[2:].zfill(32)
    left = res[:16]
    right = res[16:]
    if left.count("0") > right.count("0")*3:
        k += 1
print(k)
        