from ipaddress import *
net = ip_network("171.128.0.0/255.128.0.0",0)
k = 0
for i in net:
    res = bin(int(i))[2:].zfill(32)
    l = res[:16]
    r = res[16:]
    if l.count("1") < r.count("1"):
        k += 1
print(k) 