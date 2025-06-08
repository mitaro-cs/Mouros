from ipaddress import *
net = ip_network("192.168.156.235/255.255.255.240",0)
k = 0
for i in net.hosts():
    k += 1
    if i == ip_address("192.168.156.235"):
        print(k,i)