from ipaddress import *

'Создание ip-адресса'
ad = ip_address('адрес узла')

'Создание сети'
net = ip_network('адрес сети/маска')
net = ip_network('адрес сети/маска', 0)

'Получение адреса сети'
net.network_address

'Получение количества адресов'
net.num_addresses

'Получение маски'
net.netmask

'Перебор ip-адресов сети'
for ad in net:
    pass

'Перебор масок'
for mask in range(33):
    net = ip_network('адрес узла/' + str(mask), 0)

'Преобразование ip-адреса в двоичное представление'
ad = ip_address('адрес')
bin(int(ad))[2:].zfill(32)
