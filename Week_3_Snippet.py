import telnetlib

#Router IP Address
router = "172.16.1.1"

#Put in User information
user = 'admin'
password = 'admin'

#Telnet into the router
tn = telnetlib.Telnet(router)

#Enter Login details into the CLI
tn.read_until("Username: ")
tn.write(user + "\n")
tn.read_until("Password: ")
tn.write(password + "\n")

#Enter Configure Terminal Mode
tn.write("conf t\n")

#Exclude Gateway address
tn.write("ip dhcp excluded-address 192.168.21.1 192.168.23.1\n")

#Configure DHCP for Accounting VLAN
tn.write("ip dhcp pool Accounting_Vlan_Pool\n")
tn.write("network 192.168.21.0 255.255.255.0\n")
tn.write("default-router 192.168.0.1\n")
tn.write("exit\n")

#Configure DHCP for Engineering VLAN
tn.write("ip dhcp pool Engineering_Vlan_Pool\n")
tn.write("network 192.168.23.0 255.255.255.0\n")
tn.write("default-router 192.168.0.1\n")
tn.write("exit\n")

#closes the connection to the router
tn.close()