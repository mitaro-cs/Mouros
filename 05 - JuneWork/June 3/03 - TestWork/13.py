# Mask = 255.255.192.0
# Ip   = 192.168.0.0
from ipaddress import *
for a in range(16,25):
    net = ip_network(f"192.168.0.0/{a}",0)
    