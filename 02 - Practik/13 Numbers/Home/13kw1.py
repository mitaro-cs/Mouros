from ipaddress import *
net = ip_network("172.17.167.18/255.255.240.0",0)
for ad in net.hosts():
    print(ad)