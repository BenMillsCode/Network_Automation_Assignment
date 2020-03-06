import netmiko

def sshConnection(devices):

    connections = []

    if type(devices) == list:

         for device in devices:
                
              connections.append(netmiko.ConnectHandler(**device))

         return connections

    else:
        return netmiko.ConnectHandler(**devices)