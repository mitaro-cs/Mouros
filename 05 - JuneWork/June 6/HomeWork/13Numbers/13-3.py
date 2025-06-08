from ipaddress import *
k = 0
net = ip_network("156.132.15.138/255.255.252.0",0)
for i in net:
    k += 1
    if i == ip_address("156.132.15.138"):
        print(k)