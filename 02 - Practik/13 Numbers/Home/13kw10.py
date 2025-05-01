from ipaddress import *

for a in range(0,33):
    net1 = ip_network(f"118.187.59.255/{a}",0)
    net2 = ip_network(f"118.187.65.115/{a}",0)
    if net1.network_address != net2.network_address:
        print(a)
        break