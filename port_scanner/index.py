from models import ip as ip_model
import json

import tqdm

def scan_ips(ips):
    ips_dict = {}
    for i in tqdm(range(0, len(ips)), desc ="Text You Want"):
        ip = ips[i]
        ip_modeli = ip_model(ip)
        ip_modeli.scan_ports()
        ips_dict[ip] = str(ip_modeli)

    
    return ips_dict
