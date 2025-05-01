from ipaddress import *

net = ip_network("146.212.200.55/255.255.240.0",0)
print(net.network_address)