from ipaddress import *

net = ip_network("162.198.0.157/255.255.255.224",0)
k = 0
for ad in net.hosts():
    k += 1
    if ad == ip_address("162.198.0.157"):
        print(ad,k)