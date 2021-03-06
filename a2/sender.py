from packet import Packet
import socket, sys, os, threading

# initalize logfiles
seg_log = open("segnum.log", "a")
ack_log = open("ack.log", "a")

# configure variables
# user inputed
net_host_addr = sys.argv[1] 
net_rcv_port = int(sys.argv[2])
local_rcv_port = int(sys.argv[3]) 
timeout_intv = int(sys.argv[4]) 
payload = sys.argv[5] 

#print (net_host_addr, net_rcv_port,local_rcv_port, timeout_intv, payload)

# global
char_limit = 500 
packets = [] 
total_packets = 0
win_size = 1 
pack_size = 1024
waking = False 
confirmed = 0 
seq_cntr = 0 

# locks for multi threading
lock = threading.Lock() 
cv = threading.Condition(lock) 

# Load data
try:
    payload_file = open(payload, 'r')
except IOError:
    sys.stderr.write("ERROR: Could not open the file")
    raise SystemExit

# create packets from data and add to list
packet_data = payload_file.read(char_limit) 
while(packet_data):
    packets.append(Packet(1, total_packets, len(packet_data), packet_data))
    packet_data = payload_file.read(char_limit)
    total_packets += 1

# initiate socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', net_rcv_port))


# Reciever for ACKs
def receiver():
    global confirmed
    global waking
 
    while(True):
        
        # Recieve Packet and parse data
        newpacket = sock.recvfrom(pack_size)[0]
        newpacket = Packet.decode(Packet(newpacket))
        packet_type = newpacket[0]
        packet_seq_num = newpacket[1]
        packet_len = newpacket[2]
        packet_data = newpacket[3]

        
        lock.acquire()

        if (packet_type == 2): # EOT
            ack_log.write(str(packet_seq_num) + "\n")
            lock.release()
            return
        elif (packet_type == 1): # data
            lock.release()
            sys.stderr.write("ERROR: Unexpected Data received.")
            raise SystemExit
        else: 
            ack_log.write(str(packet_type) + "\n")
            if (packet_seq_num >= confirmed):
                confirmed = packet_seq_num + 1
                waking = True
                cv.notify_all()
            
            lock.release()
            
        

recthread = threading.Thread(target=receiver, args=())
recthread.setDaemon(True)
recthread.start()
    
while (confirmed < total_packets):
    lock.acquire()
    
    while(seq_cntr < confirmed + win_size and seq_cntr < total_packets):
        sock.sendto(Packet.encode(packets[seq_cntr]), (net_host_addr, net_rcv_port))
        seg_log.write(str(seq_cntr) + "\n")
        seq_cntr += 1
        
    cv.wait(timeout_intv)
 
    # increment counter
    if not waking:
        seq_cntr = confirmed + 1

    waking = False
    lock.release()

# send EOT, close recieving threads
sock.sendto(Packet.encode(Packet(2, seq_cntr, 0, "")), (net_host_addr, net_rcv_port))
recthread.join()
sock.close()

# close log files
seg_log.close()
ack_log.close()