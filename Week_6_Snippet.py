import netmiko, re

three_routers = [{
    "host":"209.165.200.233",
    "username":"admin",
    "password":"admin",
    "device_type":"cisco_ios"
    }, {
    "host":"172.16.1.1",
    "username":"admin",
    "password":"admin",
    "device_type":"cisco_ios"
    }, {
    "host":"192.168.2.1",
    "username":"admin",
    "password":"admin",
    "device_type":"cisco_ios"
    }]

#Connect to each Router using a loop
for router in three_routers:

    #Connect to a Router
    connected = netmiko.ConnectHandler(**router)

    #Start a Python list of commands
    ospf_set = ["router ospf 1"]

    #Receive Routing information 
    output = connected.send_command("show ip route connected")

    #Find the networks and Subnet mask using Regular Expression
    networks = re.findall("\d+\.\d+\.\d+\.\d+/\d\d", output)

    #Go through the networks found with Regular Expression in a loop
    for network in networks:

        #Split the network IP address and Subnet Mask from each other 
        net_ip, slash_mask = network.split("/")[0], int(network.split("/")[1])

        #Change Slash notation into Binary Subnet Mask
        bin_mask = ("0" * slash_mask) + ("1" * (32 - slash_mask))

        #Split the binary number into a list of 4 sets of 8 bits
        #Convert it from binary to base 10 this makes a wildcard mask for OSPF
        new_mask = [int(bin_mask[:8], 2), int(bin_mask[8:16], 2), 
                    int(bin_mask[16:24], 2), int(bin_mask[24:], 2)]

        #convert the base 10 intergers into string
        new_mask = list(map(str, new_mask))

        #Put the IP and new wildcard mask into a OSPF Network Command 
        #and add it to the Python list of OSPF commands
        ospf_set.append("network " + net_ip + " " + ".".join(new_mask) + " area 0")
    
    #Send the list of commands to the Router
    connected.send_config_set(ospf_set)

    #Disconnect from the Router
    connected.disconnect()
