from ipaddress import *

net = ip_network("126.185.90.162/255.255.252.0",0)
k = 0
for ad in net: # Host для того что бы не брать первый адрес (0000)
    k += 1
    if ad == ip_address("126.185.90.162"):
        print(ad,k)