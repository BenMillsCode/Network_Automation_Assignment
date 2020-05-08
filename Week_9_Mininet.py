from mininet.topo import Topo

class ANTTopology(Topo):

    def __init__(self):
        Topo.__init__(self)
        # Add hosts
        R1 = self.addHost('R1')
        R2 = self.addHost('R2')
        R3 = self.addHost('R3')

        S0 = self.addSwitch( 'S0' )
        S1 = self.addSwitch( 'S1' )

        PCA = self.addHost('PCA', ip="192.168.21.2/24")
        PCB = self.addHost( 'PCB', ip="192.168.23.2/24")

        ManPC = self.addController('ManPC', ip="209.165.200.238/29" )

        # Add links
        self.addLink(R2, ManPC)
        self.addLink(R2, R1)
        self.addLink(R2, R3)

        self.addLink(R1, S0)

        self.addLink(S0, PCA)
        self.addLink(S0, S1)

        self.addLink(S1, PCB)

topos = {'ANTTopology': (lambda: ANTTopology())}