#!/usr/bin/python

"""Topology with 10 switches and 10 hosts
"""

from mininet.cli import CLI
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel


class CSLRTopo( Topo ):

        def __init__( self ):
                "Create Topology"

                # Initialize topology
                Topo.__init__( self )

                # Add hosts
                h0 = self.addHost( 'Alice' )
                h1 = self.addHost( 'h1' )
                h2 = self.addHost( 'h2' )
                h3 = self.addHost( 'h3' )

                # Add switches
                s1 = self.addSwitch( 's1', listenPort=6635 )
                s2 = self.addSwitch( 's2', listenPort=6636 )
                s3 = self.addSwitch( 's3', listenPort=6637 )

                # Add Routers
                r1 = self.addSwitch( 'r1', listenPort=6638  )
                r2 = self.addSwitch( 'r2' )


                # Add links between hosts and switches
                self.addLink( h0, s1 ) # h0-eth0 <-> s0-eth1
                self.addLink( h1, s2 ) # h1-eth0 <-> s1-eth1
                self.addLink( h2, s2 ) # h2-eth0 <-> s2-eth1
                self.addLink( h3, s3 ) # h3-eth0 <-> s3-eth1

                # Add links between switches and routers
                self.addLink( s1, r1 ) # h0-eth0 <-> s0-eth1
                self.addLink( s2, r1 ) # h1-eth0 <-> s1-eth1
                self.addLink( s2, r2 ) # h2-eth0 <-> s2-eth1
                self.addLink( s3, r2 ) # h3-eth0 <-> s3-eth1



def run():
        "Create and configure network"
        topo = CSLRTopo()
        net = Mininet( topo=topo, link=TCLink, controller=None )

        # Set interface IP and MAC addresses for hosts
        h0 = net.get( 'Alice' )
        h0.intf( 'Alice-eth0' ).setIP( '10.1.1.17', 24 )
        h0.intf( 'Alice-eth0' ).setMAC( 'AA:AA:AA:AA:AA:AA' )

        h1 = net.get( 'h1' )
        h1.intf( 'h1-eth0' ).setIP( '10.4.4.48', 24 )
        h1.intf( 'h1-eth0' ).setMAC( 'b0:b0:b0:b0:b0:b0' )

        h2 = net.get( 'h2' )
        h2.intf( 'h2-eth0' ).setIP( '10.0.2.2', 24 )
        h2.intf( 'h2-eth0' ).setMAC( '0A:00:02:02:00:00' )

        h3 = net.get( 'h3' )
        h3.intf( 'h3-eth0' ).setIP( '10.0.3.2', 24 )
        h3.intf( 'h3-eth0' ).setMAC( '0A:00:03:02:00:00' )

        # Set interface MAC address for switches (NOTE: IP
        # addresses are not assigned to switch interfaces)
        s1 = net.get( 's1' )
        s1.intf( 's1-eth1' ).setMAC( '0A:00:01:01:00:01' )
        s1.intf( 's1-eth2' ).setMAC( '0A:00:0A:FE:00:02' )

        s2 = net.get( 's2' )
        s2.intf( 's2-eth1' ).setMAC( '0A:00:02:01:00:01' )
        s2.intf( 's2-eth2' ).setMAC( '0A:00:0B:FE:00:02' )
        s2.intf( 's2-eth3' ).setMAC( '0A:00:0D:01:00:03' )
        #s2.intf( 's2-eth4' ).setMAC( '0A:00:0C:FE:00:04' )

        s3 = net.get( 's3' )
        s3.intf( 's3-eth1' ).setMAC( '0A:00:03:01:00:01' )
        #s3.intf( 's3-eth2' ).setMAC( '0A:00:0D:FE:00:02' )

        # Set interface IP and MAC address for routers 
        r1 = net.get( 'r1' )
        #r1.intf( 'r1-eth0' ).setIP( '10.1.1.1', 24 )
        r1.intf( 'r1-eth1' ).setMAC( '0A:01:0A:01:0A:01' )
        #r1.intf( 'r1-eth1' ).setIP( '10.1.2.1', 24 )
        r1.intf( 'r1-eth2' ).setMAC( '0A:01:0A:01:0A:02' )




        net.start()

        # Add routing table entries for hosts (NOTE: The gateway
		# IPs 10.0.X.1 are not assigned to switch interfaces)
        h0.cmd( 'route add default gw 10.1.1.14 dev Alice-eth0' )
        h1.cmd( 'route add default gw 10.0.1.1 dev h1-eth0' )
        h2.cmd( 'route add default gw 10.0.2.1 dev h2-eth0' )
        h3.cmd( 'route add default gw 10.0.3.1 dev h3-eth0' )


        # Add arp cache entries for hosts
        h0.cmd( 'arp -s 10.1.1.14 0A:00:00:01:00:01 -i Alice-eth0' )
        h1.cmd( 'arp -s 10.0.1.1 0A:00:01:01:00:01 -i h1-eth0' )
        h2.cmd( 'arp -s 10.0.2.1 0A:00:02:01:00:01 -i h2-eth0' )
        h3.cmd( 'arp -s 10.0.3.1 0A:00:03:01:00:01 -i h3-eth0' )


        # Open Mininet Command Line Interface
        CLI(net)

        # Teardown and cleanup
        net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
