from config import ports
import socket

import json

class ip():
    def __init__(self, ip):
        self.ip = ip # IP of target
        self.open_ports = list() # List of open ports
        self.can_connect = True # Is able to connect to host
        self.hostname_exists = True # Does hostname exist

    def __str__(self):
        return json.dumps({"ip": self.ip, "open_ports": self.open_ports, "can_connect": self.can_connect, "hostname_exists": self.hostname_exists})

    def scan_ports(self):
        try:
        # will scan ports in list ports
            for port in ports:
                result_code = self.connect(port)
                if result_code == 0:
                    self.open_ports.append(port)

        except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            self.hostname_exists = False

        except socket.error:
            print("\n Server not responding !!!!")
            self.can_connect = False

    def connect(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator
        result = s.connect_ex((self.ip, port))
        if result == 0:
            return 0
        s.close()
        return 1
