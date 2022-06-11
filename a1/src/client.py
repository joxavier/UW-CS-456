from socket import *
import sys

exitCMD = "EXIT"

# validate parameters
if len(sys.argv) < 5:
    print ("ERROR: Expected 4 parameter <server_Address>, <n_port>, <req_code>, <msg>")
    exit(-1)

# type check parameters
try:
    serverAddress= str(sys.argv[1])
    n_port = int(sys.argv[2])
    req_code = int(sys.argv[3])
    messages = sys.argv[4:]
except ValueError:
    print('ERROR: check type of parameters')
    exit(-2)

### Stage 1. Negotiation using TCP sockets ### 

# configure TCP socket
clientSocketTCP = socket(AF_INET, SOCK_STREAM)
clientSocketTCP.connect((serverAddress, n_port))
clientSocketTCP.send(str(req_code).encode())

# receive r_port from server
r_port = int(clientSocketTCP.recv(1024).decode())

# close the TCP connection
clientSocketTCP.close()

### Stage 2. Transaction using UDP sockets ###

# configure UDP socket
clientSocketUDP = socket(AF_INET, SOCK_DGRAM)

# send each messages and output results
for msg in messages:
    clientSocketUDP.sendto(msg.encode(), (serverAddress, r_port))
    response = (clientSocketUDP.recvfrom(2048)[0]).decode()
    print(response)

# send exit message
clientSocketUDP.sendto(exitCMD.encode(), (serverAddress, r_port))

# close the UDP connection
clientSocketUDP.close()



