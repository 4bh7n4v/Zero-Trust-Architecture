from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.link import TCLink
from mininet.log import setLogLevel

def customTopology():
    net = Mininet(controller=Controller, switch=OVSKernelSwitch, link=TCLink)

    # Adding controllers
    c0 = net.addController('c0', controller=Controller, port=6633)  # Local controller
    c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.1', port=6634)  # Remote controller

    # Adding switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    # Adding hosts
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')

    # Adding links
    net.addLink(h1, s1)
    net.addLink(h2, s2)
    net.addLink(s1, s2)

    # Start network
    net.build()
    c0.start()
    c1.start()

    # Link switches to controllers
    s1.start([c0])  # s1 connects to c0
    s2.start([c1])  # s2 connects to c1

    # Run CLI
    net.start()
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    customTopology()
