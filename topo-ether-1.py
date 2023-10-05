import atexit
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.log import info,setLogLevel
from mininet.link import TCLink
net = None

def create_topo():
    topo = Topo()

    # Creating hosts
    for i in range(8):
        topo.addHost(f'h{i+1}')

    # Creating switches
    topo.addSwitch('core1')
    topo.addSwitch('d1')
    topo.addSwitch('d2')
    topo.addSwitch('a1')
    topo.addSwitch('a2')
    topo.addSwitch('a3')
    topo.addSwitch('a4')

    # Creating links
    topo.addLink('core1', 'd1', bw=10000, delay='1ms')
    topo.addLink('core1', 'd2', bw=10000, delay='1ms')
    topo.addLink('d1', 'a1', bw=1000, delay='3ms')
    topo.addLink('d1', 'a2', bw=1000, delay='3ms')
    topo.addLink('d2', 'a3', bw=1000, delay='3ms')
    topo.addLink('d2', 'a4', bw=1000, delay='3ms')
    topo.addLink('a1', 'h1', bw=100, delay='5ms')
    topo.addLink('a1', 'h2', bw=100, delay='5ms')
    topo.addLink('a2', 'h3', bw=100, delay='5ms')
    topo.addLink('a2', 'h4', bw=100, delay='5ms')
    topo.addLink('a3', 'h5', bw=100, delay='5ms')
    topo.addLink('a3', 'h6', bw=100, delay='5ms')
    topo.addLink('a4', 'h7', bw=100, delay='5ms')
    topo.addLink('a4', 'h8', bw=100, delay='5ms', loss=15)

    return topo

def start_nework():
    topo = create_topo()
    global net
    net = Mininet(topo=topo,autoSetMacs=True, link=TCLink)
    net.start()
    CLI(net)

def stop_network():
    if net is not None:
        net.stop()

if __name__ == '__main__':
	atexit.register(stop_network)
	setLogLevel('info')
	start_nework()
