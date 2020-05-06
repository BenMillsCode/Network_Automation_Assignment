import json

APIrequest = '{"response":[{"vlanNumber":500,"numberOfIPs":256,"ipAddress":"172.28.97.155","prefix":"24","interfaceName":"Vlan500", "networkAddress":"172.28.97.0"},{"vlanNumber":300,"numberOfIPs":4,"ipAddress":"212.1.20.1","prefix":"30","interfaceName":"Vlan300","networkAddress":"212.1.20.0"},{"vlanNumber":1,"interfaceName":"Vlan1"},{"vlanNumber":200,"numberOfIPs":256,"ipAddress":"10.1.12.1","prefix":"24","interfaceName":"Vlan200","networkAddress":"10.1.12.0"},{"vlanNumber":400,"numberOfIPs":256,"ipAddress":"10.1.14.1","prefix":"24","interfaceName":"Vlan400","networkAddress":"10.1.14.0"}],"version":"1.0"}'

#Convert JSON API request to a Python dictionary
response = json.loads(APIrequest)['response']

#Run through the list of Vlan Dictionaries
for vlan in response:

    #Print the number of the Vlan that is being investigated
    print("Vlan " + str(vlan['vlanNumber']) + " Information:")

    #If the Vlan Dictionary has a key 'ipAddress'
    if "ipAddress" in vlan:

        #Print the Vlan IP address and Prefix information
        print('IP Address: ' + vlan['ipAddress'] +
                "\nSubnet Prefix: " + vlan['prefix'] + '\n')

    #If an IP Address key doesn't exist, print that the information isn't available
    else:
        print('IP Address: No IP\n' 'Prefix: No Prefix')