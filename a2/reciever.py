from packet import Packet
import socket, sys

# initalize logfiles
arr_log = open("arrival.log", "a")

# configure variables
# user inputed
net_host_addr = sys.argv[1]
net_rcv_port = int(sys.argv[2])
local_rcv_port = int(sys.argv[3])
output_file = sys.argv[4]

# global
expected = 0 
confirmed = None 
pack_size = 1024 

# open output file
try:
    payload_file = open(output_file, 'a')
except IOError:
    sys.stderr.write("ERROR: cannot write to output file.")
    raise SystemExit

# initiate socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', local_rcv_port))

# recieve packets
while(True):
    pack = sock.recvfrom(pack_size)[0]
    packet = Packet.decode(Packet(pack))
    packet_type = packet[0]
    packet_seq_num = packet[1]
    packet_len = packet[2]
    packet_data = packet[3]

    # log recieved packet
    arr_log.write(str(packet_seq_num) + "\n")
    
    # check packet sequence
    if (packet_seq_num == expected): 
        if (packet_type == 2): # EOT
            #return EOT
            sock.sendto(Packet.encode(Packet(2, packet_seq_num, 0, "")), (net_host_addr, net_rcv_port))
            break
        elif (packet_type == 1): # Data
            # write payload to file, and return ACK
            payload_file.write(packet_data)
            sock.sendto(Packet.encode(Packet(0, packet_seq_num, 0, "")), (net_host_addr, net_rcv_port))
            
            # increment counter
            confirmed = packet_seq_num
            expected = confirmed + 1
            
    elif (confirmed):
        # unexpected sequence number, return last correct ACK
        sock.sendto(Packet.encode(Packet(0, confirmed, 0, "")), (net_host_addr, net_rcv_port))
        

arr_log.close()