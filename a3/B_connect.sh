#!/usr/bin/env bash

# Sets bridge s0 to use OpenFlow 1.3


# Sets bridge s1 to use OpenFlow 1.3
ovs-vsctl set bridge s1 protocols=OpenFlow13 

# Sets bridge r1 to use OpenFlow 1.3
ovs-vsctl set bridge r1 protocols=OpenFlow13

# Sets bridge s2 to use OpenFlow 1.3
ovs-vsctl set bridge s2 protocols=OpenFlow13



# Print the protocols that each switch supports
for switch in s1 r1 s2;
do
    protos=$(ovs-vsctl get bridge $switch protocols)
    echo "Switch $switch supports $protos"
done

# Avoid having to write "-O OpenFlow13" before all of your ovs-ofctl commands.
ofctl='ovs-ofctl -O OpenFlow13'


# OVS rules for switch 1
# h1 -> h4
$ofctl add-flow s1 \
    in_port=1,ip,nw_src=10.0.1.2,nw_dst=10.0.3.2,actions=mod_dl_src:0A:00:0C:01:00:03,mod_dl_dst:0A:00:0D:01:00:03,output=2

# h4 -> h1
$ofctl add-flow s1 \
    in_port=2,ip,nw_src=10.0.3.2,nw_dst=10.0.1.2,actions=mod_dl_src:0A:00:01:01:00:01,mod_dl_dst:aa:aa:aa:aa:aa:aa,output=1 

# OVS rules for switch 2

# h1 -> h4
$ofctl add-flow r1 \
    in_port=2,ip,nw_src=10.0.1.2,nw_dst=10.0.3.2,actions=mod_dl_src:0A:00:0C:FE:00:04,mod_dl_dst:0A:00:0D:FE:00:02,output=3 


# h4 -> h1
$ofctl add-flow r1 \
    in_port=3,ip,nw_src=10.0.3.2,nw_dst=10.0.1.2,actions=mod_dl_src:0A:00:0D:01:00:03,mod_dl_dst:0A:00:0C:01:00:03,output=2 

# OVS rules for switch 3
# h1 -> h4
$ofctl add-flow s2 \
    in_port=2,ip,nw_src=10.0.1.2,nw_dst=10.0.3.2,actions=mod_dl_src:0A:00:0E:01:00:01,mod_dl_dst:b0:b0:b0:b0:b0:b0,output=1 


# h4 -> h1
$ofctl add-flow s2 \
    in_port=1,ip,nw_src=10.0.3.2,nw_dst=10.0.1.2,actions=mod_dl_src:0A:00:0D:FE:00:02,mod_dl_dst:0A:00:0C:FE:00:04,output=2 



# Print the flows installed in each switch
for switch in s1 r1 s2;
do
    echo "Flows installed in $switch:"
    $ofctl dump-flows $switch
    echo ""
done
