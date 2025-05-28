from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

class CustomTopo(Topo):
    def build(self):
        # Criando switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s5 = self.addSwitch('s5')

        # Criando hosts
        h1 = self.addHost('h1', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', mac='00:00:00:00:00:02')
        h3 = self.addHost('h3', mac='00:00:00:00:00:03')
        h4 = self.addHost('h4', mac='00:00:00:00:00:04')
        h5 = self.addHost('h5', mac='00:00:00:00:00:05')
        h6 = self.addHost('h6', mac='00:00:00:00:00:06')
        h7 = self.addHost('h7', mac='00:00:00:00:00:07')
        h8 = self.addHost('h8', mac='00:00:00:00:00:08')

        # Conectando hosts
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s5)
        self.addLink(h4, s5)
        self.addLink(h5, s2)
        self.addLink(h6, s3)
        self.addLink(h7, s3)
        self.addLink(h8, s3)

        # Conectando switches
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s2, s5)

def run():
    topo = CustomTopo()
    net = Mininet(topo=topo, switch=OVSSwitch, controller=None, autoSetMacs=True)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
