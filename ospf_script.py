import netmiko, re, json, sharedFunctions

print(sharedFunctions.getDevicesDicts("devices.json", 'routers'))

connected = sharedFunctions.sshConnection(devices["routers"]['R2'])

interfaces = connected.send_command('show ip interface brief')
connected.disconnect()

addresses = re.findall("\d+\.\d+\.\d+\.\d+", interfaces)

for ip in addresses:
    print(ip)