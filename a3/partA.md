
## Command #1
### Code
    $ofctl add-flow s0 \
        in_port=1,ip,nw_src=10.0.0.2,nw_dst=10.0.1.2,actions=mod_dl_src:0A:00:0A:01:00:02,mod_dl_dst:0A:00:0A:FE:00:02,output=2
### Description 
The above command adds a flow to bridge **s0** to listen on **ingresstion port 1** for **IP** traffic from source **h0** and destined to **h1**, upon recieving such packets, modify source MAC to its own, destination MAC to **s1** and foward to **output port 2** .
<br>

### Arguments
**add-flow** --> creates a flow entry  
**s0** --> host to listen for traffc on (s0)  
**in_port=1** --> ingress port (s0-eth1) on host to listen for traffc  
**ip** --> type of traffic to listen for (IP)  
**nw_src=10.0.0.2** --> foward packets from source 10.0.0.2 (h0)  
**nw_dst=10.0.1.2** --> foward packets destined to 10.0.1.2 (h1)  
**actions=mod_dl_src:0A:00:0A:01:00:02** --> modify source MAC address to one of it's own interfaces (s0-eth2)  
**mod_dl_dst:0A:00:0A:FE:00:02** --> modify dstination MAC address to one s1's interfaces (s1-eth2)  
**output=2** --> foward packet to output link 2 (s0-eth2)


# Command #2
### Code
    $ofctl add-flow s0 \
        in_port=2,ip,nw_src=10.0.1.2,nw_dst=10.0.0.2,actions=mod_dl_src:0A:00:00:01:00:01,mod_dl_dst:0A:00:00:02:00:00,output=1

### Description 
The above command adds a flow to bridge **s0** to listen on **ingresstion port 2** for IP traffic from source **h1** and destined to **h0**, upon recieving such packets, modify source MAC to its own, destination MAC to **h0** and foward to **output port 1**.
<br>

### Arguments
**add-flow** --> creates a flow entry  
**s0** --> host to listen for traffc on (s0)  
**in_port=2** --> ingress port (s0-eth2) on host to listen for traffc  
**ip** --> type of traffic to listen for (IP)  
**nw_src=10.0.1.2** --> foward packets from source 10.0.1.2 (h1)  
**nw_dst=10.0.0.2** --> foward packets destined to 10.0.0.2 (h0)  
**actions=mod_dl_src:0A:00:00:01:00:01** --> modify source MAC address to one of it's own interfaces (s0-eth1)  
**mod_dl_dst:0A:00:00:02:00:00** --> modify destination MAC address to one h0's interfaces (h0-eth0)  
**output=1** --> foward packet to output link 1 (s0-eth1)  
<br>

## Command #3
### Code
    $ofctl add-flow s1 \
        in_port=2,ip,nw_src=10.0.0.2,nw_dst=10.0.1.2,actions=mod_dl_src:0A:00:01:01:00:01,mod_dl_dst:0A:00:01:02:00:00,output=1

### Description 
The above command adds a flow to bridge **s1** to listen on **ingresstion port 2** for IP traffic from source **h0** and destined to **h1**, upon recieving such packets, modify source MAC to its own, destination MAC to **h1** and foward to **output port 1**.
<br>

### Arguments
**add-flow** --> creates a flow entry  
**s1** --> host to listen for traffc on (s1)  
**in_port=2** --> ingress port (s1-eth2) on host to listen for traffc  
**ip** --> type of traffic to listen for (IP)  
**nw_src=10.0.0.2** --> foward packets from source 10.0.0.2 (h0)  
**nw_dst=10.0.1.2** --> foward packets destined to 10.0.1.2 (h1)  
**actions=mod_dl_src:0A:00:01:01:00:01** --> modify source MAC address to one of it's own interfaces (s1-eth1)  
**mod_dl_dst:0A:00:01:02:00:00** --> modify destination MAC address to one h0's interfaces (h1-eth0)  
**output=1** --> foward packet to output link 1 (s1-eth1)  
<br>

## Command #4
### Code
    $ofctl add-flow s1 \
        in_port=1,ip,nw_src=10.0.1.2,nw_dst=10.0.0.2,actions=mod_dl_src:0A:00:0A:FE:00:02,mod_dl_dst:0A:00:0A:01:00:02,output=2

### Description 
The above command adds a flow to bridge **s1** to listen on **ingresstion port 1** for IP traffic from source **h1** and destined to **h0**, upon recieving such packets, modify source MAC to its own, destination MAC to **s0** and foward to **output port 2**.
<br>

### Arguments
**add-flow** --> creates a flow entry  
**s1** --> host to listen for traffc on (s1)  
**in_port=1** --> ingress port (s1-eth1) on host to listen for traffc  
**ip** --> type of traffic to listen for (IP)  
**nw_src=10.0.1.2** --> foward packets from source 10.0.1.2 (h1)  
**nw_dst=10.0.0.2** --> foward packets destined to 10.0.0.2 (h0)  
**actions=mod_dl_src:0A:00:0A:FE:00:02** --> modify source MAC address to one of it's own interfaces (s1-eth2)  
**mod_dl_dst:0A:00:0A:01:00:02** --> modify destination MAC address to one s0's interfaces (s0-eth2)  
**output=2** --> foward packet to output link 2 (s1-eth2)  
<br>