from flask import Flask, request

import json

def get_targets():
    with open("port_scanner/ips.json") as f:
        data = json.load(f)
    return data


def return_targets(data=get_targets()) -> list:
    to_attack = []
    for itemi in data["ip"]:
        for item in itemi:
            item = itemi[item]
            for ports in item["open_ports"]:
                if ports in [80, 443, 8080, 8443]:
                    if ports in [443, 8443]:
                        prefix = "https://"
                    else:
                        prefix = "http://"
                    
                    to_attack.append(f"{prefix}{item['ip']}:{ports}")
    return to_attack



app = Flask(__name__)

@app.route("/")
def index():
    return {"to_attack": return_targets()}

app.run()