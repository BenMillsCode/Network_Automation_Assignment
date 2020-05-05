import paramiko, jinja2, time

two_switches = [{
    "host":"192.168.99.2",
    "username":"admin",
    "password":"admin"
    },{
    "host":"192.168.99.3",
    "username":"admin",
    "password":"admin"        
    }
    ]

vlans = [
    {'number':'21', 'name':'Accounting', 'ip_add':"192.168.21.", 'mask':'255.255.255.0'},
    {'number':'23', 'name':'Engineering', 'ip_add':"192.168.23.",'mask':'255.255.255.0'},
    {'number':'99', 'name':'Management', 'ip_add':"192.168.99.", 'mask':'255.255.255.0'}
]

#Create paramiko SSH client and add SSH keys
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ENV = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
template = ENV.get_template("Week_5_Jinja_Snippet.j2")

#Connect to the switches using a loop
for switch in two_switches:

    #connect to the switch
    client.connect(switch['host'], username=switch['username'], password=switch['password'])

    #create a SSH Shell
    connected = client.invoke_shell()

    ip_no = switch['host'].split('.')[3]

    #Enter Configuration Terminal mode
    connected.send('config terminal\n')

    #Start loop for vlan configuration
    for vlan in vlans:

        #create the commands from the template
        vlan_config = template.render(vlan = vlan, ip_no=ip_no)
        #send the commands
        connected.send(str(vlan_config))
        time.sleep(2)
        
    #Close the SSH shell
    connected.close()

#Close Paramiko SSH connection client
client.close()

