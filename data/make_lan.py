import socket

with open("lands.txt") as f:
    land_codes = f.read().split("\n")

def hostname_resolves(hostname):
    try:
        socket.gethostbyname(hostname)
        return 1
    except socket.error:
        return 0
lukoil = []

for code in land_codes:
    domain = f"lukoil{code}"
    status = hostname_resolves(domain)

    if status == 1:
        print(domain)
        lukoil.append(domain)

print(lukoil)