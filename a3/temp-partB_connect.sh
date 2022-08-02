#!/usr/bin/env bash

# Sets bridge s0 to use OpenFlow 1.3
ovs-vsctl set bridge s1 protocols=OpenFlow13 

# Sets bridge s1 to use OpenFlow 1.3
ovs-vsctl set bridge s2 protocols=OpenFlow13 

# Sets bridge s2 to use OpenFlow 1.3
ovs-vsctl set bridge s3 protocols=OpenFlow13

# Sets bridge s3 to use OpenFlow 1.3
ovs-vsctl set bridge r1 protocols=OpenFlow13

# Sets bridge s4 to use OpenFlow 1.3
ovs-vsctl set bridge r2 protocols=OpenFlow13 

# Print the protocols that each switch supports
for switch in s1 s2 s3 r1 r2;
do
    protos=$(ovs-vsctl get bridge $switch protocols)
    echo "Switch $switch supports $protos"
done

# Avoid having to write "-O OpenFlow13" before all of your ovs-ofctl commands.
ofctl='ovs-ofctl -O OpenFlow13'

# OVS rules for switch 0
# h0 -> h2
# Alice -> Bob
$ofctl add-flow s1 \
    in_port=*,ip,nw_src=10.1.1.17,nw_dst=10.4.4.48,actions=mod_dl_src:0A:00:0A:FE:00:02,mod_dl_dst:0A:01:0A:01:0A:01 

$ofctl add-flow r1 \
    in_port=*,ip,nw_src=10.1.1.17,nw_dst=10.4.4.48,actions=mod_dl_src:0A:01:0A:01:0A:02,mod_dl_dst:0A:00:02:01:00:01

$ofctl add-flow s2 \
    in_port=*,ip,nw_src=10.1.1.17,nw_dst=10.4.4.48,actions=mod_dl_src:0A:00:0B:FE:00:02,mod_dl_dst:b0:b0:b0:b0:b0:b0 


# Print the flows installed in each switch
for switch in s1 s2 s3 r1 r2;
do
    echo "Flows installed in $switch:"
    $ofctl dump-flows $switch
    echo ""
done
