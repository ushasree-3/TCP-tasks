from mininet.topo import Topo
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI

class Topology(Topo):
    def build(self, loss=0):  # Link loss parameter added (default 0)
        # Create switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # Create hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')  # TCP Server

        # Connect hosts to switches
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s3)
        self.addLink(h5, s3)
        self.addLink(h6, s4)
        self.addLink(h7, s4)  # H7 is the server

        # Configure links with bandwidth and loss
        self.addLink(s1, s2, bw=100)  # 100Mbps S1-S2
        self.addLink(s2, s3, bw=50, loss=loss)  # 50Mbps S2-S3 with loss
        self.addLink(s3, s4, bw=100)  # 100Mbps S3-S4

if __name__ == '__main__':
    for loss in [1, 5]:  # Run tests for 1% and 5% loss
        print(f"Running topology with {loss}% loss on S2-S3")
        net = Mininet(topo=Topology(loss=loss), link=TCLink)
        net.start()
        CLI(net)  # Keep Mininet CLI open for testing
        net.stop()
