from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.link import TCLink

def twoSwitchTopology():
    net = Mininet(controller=Controller, switch=OVSKernelSwitch, link=TCLink)

    print("*** Adding controller")
    c0 = net.addController('c0')

    print("*** Adding switches")
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    print("*** Adding hosts")
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')

    print("*** Creating links")
    net.addLink(h1, s1)
    net.addLink(h2, s2)
    net.addLink(s1, s2)  # Inter-switch link

    print("*** Starting network")
    net.build()
    c0.start()
    s1.start([c0])
    s2.start([c0])

    print("*** Running CLI")
    CLI(net)

    print("*** Stopping network")
    net.stop()

if __name__ == '__main__':
    twoSwitchTopology()
