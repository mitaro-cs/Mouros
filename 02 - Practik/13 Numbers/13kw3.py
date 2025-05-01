from ipaddress import *
net = ip_network("255.255.254.0/255.255.254.0",0)
print(net.num_addresses)