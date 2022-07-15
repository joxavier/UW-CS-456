from packet import Packet
import socket, sys

# save values needed to talk to host emulator
haddr = sys.argv[1] # network host address
dport = int(sys.argv[2]) # dest port on host
rport = int(sys.argv[3]) # recv port for this app
received = sys.argv[4] # filename to be used to record recvd data

# try opening the file
try:
    msgfile = open(received, 'a')
except IOError:
    sys.stderr.write("Failed to open file to write data. Stop being terrible at life pls")
    raise SystemExit

# logfile (received packets)
# at end call things.close()
arrlog = open("arrival.log", "a")

# some vars needed for execution
expected = 0 # next packet # expected
confirmed = None # last confirmed packet
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket!
sock.bind(('', rport)) # set socket to recv on rport
pack_size = 512 # packet size in bytes

# let's get this bread! I mean packets. yes, I re-used that joke.
while(True):
    pack, addr = sock.recvfrom(pack_size)
    
    # if we can't get a packet
    if (not pack):
        break
    else:
        packet = Packet.decode(Packet(pack))
        
    #snum = Packet.decode(packet)[1]
    packet_type = packet[0]
    packet_seq_num = packet[1]
    packet_len = packet[2]
    packet_data = packet[3]
    arrlog.write(str(packet_seq_num) + "\n")
    
    if (packet_seq_num == expected): # got the next packet
        if (packet_type == 2): # EOT packet
            # send EOT and exit
            sock.sendto(Packet.encode(Packet(2, packet_seq_num, 0, "")), (haddr, dport))
            break
        elif (packet_type == 1): # data packet
            # send ACK, record snum, increment expected
            sock.sendto(Packet.encode(Packet(0, packet_seq_num, 0, "")), (haddr, dport))
            confirmed = packet_seq_num
            expected = confirmed + 1
            # deal with new data
            msgfile.write(packet_data)
            
    elif (confirmed): # got wrong packet, send confirmation only of last good packet
        sock.sendto(Packet.encode(Packet(0, confirmed, 0, "")), (haddr, dport))
        

arrlog.close()