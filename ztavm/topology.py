from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from graphviz import Digraph

def visualize_topology(net):
    """Automatically generate and render the network topology."""
    dot = Digraph(comment="Network Topology")

    # Add all nodes
    for node in net.keys():
        dot.node(node, label=node)

    # Add edges
    for link in net.links:
        src, dst = link.intf1.node.name, link.intf2.node.name
        dot.edge(src, dst)

    # Render the graph
    dot.render("network_topology", format="png", cleanup=True)

def customTopology():
    net = Mininet(controller=None, switch=OVSKernelSwitch, link=TCLink)

    print("*** Creating Controllers")
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)
    c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.2', port=6634)
    sdpCtrl = net.addController('sdpCtrl', controller=Controller, ip='127.0.0.3', port=6635)

    router = net.addHost('router')

    print("*** Adding Switches")
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')
    s7 = net.addSwitch('s7')

    print("*** Adding Hosts")
    ih1 = net.addHost('ih1', ip='192.168.1.2/24')
    ih2 = net.addHost('ih2', ip='192.168.1.3/24')
    ih3 = net.addHost('ih3', ip='192.168.1.4/24')
    h7 = net.addHost('h7', ip='192.168.1.5/24')
    h8 = net.addHost('h8', ip='192.168.1.6/24')
    h9 = net.addHost('h9', ip='192.168.1.7/24')
    h10 = net.addHost('h10', ip='192.168.3.10/24') 
    h11 = net.addHost('h11', ip='192.168.3.11/24')
    ah1 = net.addHost('ah1', ip='192.168.2.4/24')
    ah2 = net.addHost('ah2', ip='192.168.2.5/24')
    sdpGw = net.addHost('sdpGw', ip='192.168.2.6/24')

    print("*** Adding Links")
    # Hosts to switches
    net.addLink(s1, ih1)
    net.addLink(s1, ih2)
    net.addLink(s1, h7)
    net.addLink(s5, ih3)
    net.addLink(s5, h9)
    net.addLink(s6, h8)
    net.addLink(s2, ah1)
    net.addLink(s2, ah2)
    # net.addLink(router, h10)
    # net.addLink(router, h11)
    net.addLink(s3, sdpGw)
    net.addLink(s7,h10)
    net.addLink(s7,h11)

    # Switch interconnections
    net.addLink(s1, s5)
    net.addLink(s5, s6)
    #net.addLink(s6, s3)
    net.addLink(s3, s2)


    # Router connections
    net.addLink(router, s6, intfName1='router-s6-eth0')
    net.addLink(router, s3, intfName1='router-s3-eth1')
    net.addLink(router, s7, intfName1='router-s7-eth2')

    print("*** Starting Network")
    net.build()
    c0.start()
    c1.start()
    sdpCtrl.start()
    s1.start([c0])
    s2.start([c1])
    s3.start([c0, sdpCtrl])
    s5.start([c1])
    s6.start([c1])
    s7.start([c0])

    print("*** Configuring Router and Hosts")
    # Router IP setup
    router.setIP('192.168.1.1/24', intf='router-s6-eth0')
    router.setIP('192.168.2.1/24', intf='router-s3-eth1')
    router.setIP('192.168.3.1/24', intf='router-s7-eth2')

    # Enable IP forwarding on the router
    router.cmd('sysctl -w net.ipv4.ip_forward=1')

    # Set default gateway for hosts in network 192.168.1.0/24
    for host in [ih1, ih2, ih3, h7, h8, h9]:
        host.cmd('ip route add default via 192.168.1.1')

    # Set default gateway for hosts in network 192.168.3.0/24
    for host in [h10, h11]:
        host.cmd('ip route add default via 192.168.3.1')

    # Set default gateway for hosts in network 192.168.2.0/24
    for host in [ah1, ah2, sdpGw]:
        host.cmd('ip route add default via 192.168.2.1')

    # Configure static routes on the router
    # router.cmd('ip route add 192.168.3.0/24 via 192.168.2.1')

    visualize_topology(net)

    print("*** Running CLI")
    CLI(net)

    print("*** Stopping Network")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    customTopology()
