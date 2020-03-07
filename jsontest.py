import json

device_file = open("devices.json", "r")

devices = json.loads(device_file.read())
print(type(devices))
print(devices["routers"]['R2'])