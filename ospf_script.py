import netmiko, re, json, sharedFunctions

import json

device_file = open("devices.json", "r")

devices = json.loads(device_file.read())

connected = sharedFunctions.sshConnection(devices["routers"]['R2'])

interfaces = connected.send_command('show ip interface brief')
connected.disconnect()

addresses = re.findall("\d+\.\d+\.\d+\.\d+", interfaces)

for ip in addresses:
    print(ip)