from models import ip as ip_model
import json
import socket

from targets import lukoil, lands_codes

from config import ports

def scan_ips(ips):
    ips_dict = {}
    for i in range(0, len(ips)):
        ip = ips[i]
        ip_modeli = ip_model(ip)
        ip_modeli.scan_ports()
        ips_dict[ip] = ip_modeli.export_data()
    
    return ips_dict

def get_ips_by_dns_lookup(target, port=None):
    '''
        this function takes the passed target and optional port and does a dns
        lookup. it returns the ips that it finds to the caller.

        :param target:  the URI that you'd like to get the ip address(es) for
        :type target:   string
        :param port:    which port do you want to do the lookup against?
        :type port:     integer
        :returns ips:   all of the discovered ips for the target
        :rtype ips:     list of strings

    '''
    ips1 = []
    for port in ports:
        for item in list(map(lambda x: x[4][0], socket.getaddrinfo('{}.'.format(target),port,type=socket.SOCK_STREAM))):
            if not item in ips1:
                ips1.append(item)
    
    return ips1

def hostname_resolves(hostname):
    try:
        socket.gethostbyname(hostname)
        return 1
    except socket.error:
        return 0

ip_add = []

domains = []

for code in lands_codes:
    domain = f"lukoil{code}"
    status = hostname_resolves(domain)

    if status == 1:
        print(domain)
        lukoil.append(domain)


for target in lukoil:
    ips = get_ips_by_dns_lookup(target=target)
    for ip in ips:
        if not ip in ip_add:
            ip_add.append(ip)
print(ip_add)
ip_data = {}
for ip in ip_add:
    data = scan_ips([ip])[ip]
    ip_data[ip] = scan_ips([ip])
    print(data)

with open("ips.json", "w") as f:
    json.dump(ip_data, f)
