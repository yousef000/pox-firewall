#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

class final_topo(Topo):
  def build(self):
    
    # Examples!
    # Create a host with a default route of the ethernet interface. You'll need to set the
    # default gateway like this for every host you make on this assignment to make sure all 
    # packets are sent out that port. Make sure to change the h# in the defaultRoute area
    # and the MAC address when you add more hosts!
    h10 = self.addHost('h10',mac='00:00:00:00:00:01',ip='10.0.1.10', defaultRoute="h10-eth0")
    h20 = self.addHost('h20',mac='00:00:00:00:00:02',ip='10.0.2.20', defaultRoute="h20-eth0")
    h30 = self.addHost('h30',mac='00:00:00:00:00:03',ip='10.0.3.30', defaultRoute="h30-eth0")
    h40 = self.addHost('h40',mac='00:00:00:00:00:04',ip='10.0.4.40', defaultRoute="h40-eth0")
    h50 = self.addHost('h50',mac='00:00:00:00:00:05',ip='10.0.5.50', defaultRoute="h50-eth0")
    h60 = self.addHost('h60',mac='00:00:00:00:00:06',ip='10.0.6.60', defaultRoute="h60-eth0")
    h70 = self.addHost('h70',mac='00:00:00:00:00:07',ip='10.0.7.70', defaultRoute="h70-eth0")
    h80 = self.addHost('h80',mac='00:00:00:00:00:08',ip='10.0.8.80', defaultRoute="h80-eth0")
    server = self.addHost('server',mac='00:00:00:00:00:09',ip='10.0.9.10', defaultRoute="server-eth0")
    untrusted = self.addHost('untrusted',mac='00:00:00:00:00:10',ip='10.0.0.90/24', defaultRoute="untrusted-eth0")

    # Create a switch. No changes here from Lab 1.
    s1 = self.addSwitch('s1')       # floor 1 switch 1
    s2 = self.addSwitch('s2')       # floor 1 switch 2
    s3 = self.addSwitch('s3')       # floor 2 switch 1
    s4 = self.addSwitch('s4')       # floor 2 switch 2
    d5 = self.addSwitch('d5')       # data center switch
    c6 = self.addSwitch('c6')       # core switch

    # Connect Port 8 on the Switch to Port 0 on Host 1 and Port 9 on the Switch to Port 0 on 
    # Host 2. This is representing the physical port on the switch or host that you are 
    # connecting to.
    self.addLink(s1,h10, port1=1, port2=0)
    self.addLink(s1,h20, port1=2, port2=0)
    self.addLink(s2,h30, port1=1, port2=0)
    self.addLink(s2,h40, port1=2, port2=0)
    self.addLink(s3,h50, port1=1, port2=0)
    self.addLink(s3,h60, port1=2, port2=0)
    self.addLink(s4,h70, port1=1, port2=0)
    self.addLink(s4,h80, port1=2, port2=0)
    self.addLink(c6,s1, port1=1, port2=3)
    self.addLink(c6,s2, port1=2, port2=3)
    self.addLink(c6,s3, port1=3, port2=3)
    self.addLink(c6,s4, port1=4, port2=3)
    self.addLink(c6,untrusted, port1=5, port2=0)
    self.addLink(d5,c6, port1=3, port2=6)
    self.addLink(d5,server, port1=1, port2=0)

def configure():
  topo = final_topo()
  net = Mininet(topo=topo, controller=RemoteController)
  net.start()

  CLI(net)
  
  net.stop()


if __name__ == '__main__':
  configure()
