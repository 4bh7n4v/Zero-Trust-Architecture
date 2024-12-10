from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def customTopology():
    #net = Mininet(controller=Controller, switch=OVSKernelSwitch, link=TCLink)  #controller is define when to chose one of n or any of n
    net = Mininet(controller=None, switch=OVSKernelSwitch, link=TCLink) #none for using all
    print("*** Creating Controllers")
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)
    c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.2', port=6634)

    print("*** Adding switches")
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')

    print("*** Assigning Controllers")
    # Assign specific controllers to switches
    net.get('s1').start([c1])  # s1 connected to c1
    net.get('s5').start([c1])  # s5 connected to c1
    net.get('s6').start([c1])  # s6 connected to c1
    net.get('s2').start([c0])  # s2 connected to c0
    net.get('s3').start([c0])  # s3 connected to c0

    print("*** Adding hosts")
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    h3 = net.addHost('h3', ip='10.0.0.3/24')
    h7 = net.addHost('h7', ip='10.0.0.7/24')
    h8 = net.addHost('h8', ip='10.0.0.8/24')
    h9 = net.addHost('h9', ip='10.0.0.9/24')
    h10 = net.addHost('h10', ip='10.0.0.10/24')
    h11 = net.addHost('h11', ip='10.0.0.11/24')
    ah1 = net.addHost('ah1', ip='10.0.0.21/24')  # Hidden service 1
    ah2 = net.addHost('ah2', ip='10.0.0.22/24')  # Hidden service 2
    sdpCtrl = net.addHost('sdpCtrl', ip='10.0.0.30/24')  # Simplified name
    sdpGw = net.addHost('sdpGw', ip='10.0.0.31/24')      # Simplified name

    print("*** Adding links")
    net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s1, h7)
    net.addLink(s1, h8)
    net.addLink(s1, h9)

    net.addLink(s2, ah1)
    net.addLink(s2, ah2)

    net.addLink(s3, h10)
    net.addLink(s3, h11)
    net.addLink(s3, sdpCtrl)  # Updated host name
    net.addLink(s3, sdpGw)   # Updated host name

    net.addLink(s1, s5)
    net.addLink(s5, s6)
    net.addLink(s6, s3)

    net.addLink(s3, s2)

    print("*** Starting network")
    net.build()
    c0.start()
    c1.start()
    s1.start([c0])
    s2.start([c0])
    s3.start([c0])
    s5.start([c1])
    s6.start([c1])

    print("*** Running CLI")
    CLI(net)

    print("*** Stopping network")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    customTopology()
