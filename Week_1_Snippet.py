import getpass, sys, telnetlib

#Router IP Address
router = "172.16.1.1"

#Get Telnet username from user
user = raw_input("Enter your Telnet username: ")
password = getpass.getpass()
tn = telnetlib.Telnet(HOST)
tn.read_until("Username: ")
tn.write(user + "\n")

if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

    tn.write("conf t\n")

    tn.write("ip dhcp excluded-address 192.168.21.1 192.168.23.1\n")
    tn.write("ip dhcp pool Account_Vlan_Pool\n")
    tn.write("network 192.168.21.0 255.255.255.0\n")
    tn.write("default-router 192.168.0.1\n")
    tn.write("exit\n")

    tn.write("ip dhcp excluded-address 192.168.21.1 192.168.23.1\n")
    tn.write("ip dhcp pool Engineering_Vlan_Pool\n")
    tn.write("network 192.168.23.0 255.255.255.0\n")
    tn.write("default-router 192.168.0.1\n")
    tn.write("exit\n")
    print tn.read_all()