from mininet.net import Mininet
from mininet.topo import Topo
from mininet.link import TCLink

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Add switch
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(s2, s3)
        self.addLink(h4, s3)
        self.addLink(s1, s2)

# Create the network
net = Mininet(topo=MyTopo(), link=TCLink)

# Start the network
net.start()

# Run the pingall command
net.pingAll()

# Stop the network
net.stop()
