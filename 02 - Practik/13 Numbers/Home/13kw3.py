from ipaddress import *
net = ip_network("255.255.255.192/255.255.255.192",0)
print(net.num_addresses)
