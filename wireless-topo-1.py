from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.cli import CLI
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference


def start_topology():

    # Instanciating the network
    net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference)

    # Creating stations
    net.addStation('sta1', position='40,40,0')
    net.addStation('sta2', position='60,70,0')
    net.addStation('sta2', position='30,70,0')

    net.addAccessPoint('ap1', ssid='my-ssid', mode='a', channel="36",
                       failMode='standalone', position='80,80,0')


    # Setting up propagation mode
    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=4)


    # Plotting wireless topology graph
    info("*** Plotting graphs\n")
    net.plotGraph(max_x=100, max_y=100)

    # Running enviroment
    #==================================#
    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Starting network\n")
    net.build()

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    start_topology()
