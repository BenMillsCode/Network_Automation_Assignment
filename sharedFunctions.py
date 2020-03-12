import netmiko, json

def sshConnection(devices):

    connections = []

    if type(devices) == list:

         for device in devices:
                
              connections.append(netmiko.ConnectHandler(**device))

         return connections

    else:
        return netmiko.ConnectHandler(**devices)

def getDevicesDicts(device_file, device_type):

     device_file = open(device_file, "r")

     devices = json.loads(device_file.read())[device_type]

     devices_keys =  devices.keys()

     devices_dicts = []

     for key in devices_keys:
          
          devices_dicts.append(devices[key])

     return devices_dicts