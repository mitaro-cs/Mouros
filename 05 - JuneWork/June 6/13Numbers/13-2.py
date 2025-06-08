from ipaddress import *
k = 0
net = ip_network("156.128.0.227/255.255.255.248",0)
for i in net.hosts():
    k += 1
    if i == ip_address("156.128.0.227"):
        print(i,k)