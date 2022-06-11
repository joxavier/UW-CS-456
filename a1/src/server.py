from socket import *
import sys


isExit = False
exitCMD = "EXIT"

# Validate parameters
if len(sys.argv) != 2:
    print ("ERROR: Expected a single parameter <req_code>")
    exit(-1)

# type check parameters
try:
    req_code = int(sys.argv[1])
except ValueError:
    print('ERROR: <req_code> should be an integer!')
    exit(-2)

### Stage 1. Negotiation using TCP sockets ### 

# 1. create server-side TCP socket with a random <n_port>
serverSocketTCP = socket(AF_INET, SOCK_STREAM)
serverSocketTCP.bind(("", 0))
serverSocketTCP.listen(1)

# output n_port
n_port = serverSocketTCP.getsockname()[1]
print('SERVER_TCP_PORT=%d' % n_port)

# listening for req_code from client
while True:
    connectionSocket, clientAddress = serverSocketTCP.accept()
    message = connectionSocket.recv(1024).decode()
    
    #verify valid req_code
    try:
        client_req_code = int(message)
    except ValueError:
        print('ERROR: Expected to receive a <req_code> as an integer. Got ' + type(message))
        exit(-2)

    if client_req_code != req_code:
        print('Incorrect req_code sent from client: %d' % client_req_code)
        connectionSocket.close()
        exit()

    ### Stage 2. Transaction using UDP sockets ###

    print("Client request code is a match. Server is sending <r_port>.") 

    # configure UDP socket
    serverSocketUDP = socket(AF_INET, SOCK_DGRAM)
    serverSocketUDP.bind(('', 0))

    # get r_port and send to client
    r_port = str(serverSocketUDP.getsockname()[1])
    connectionSocket.send(r_port.encode())

    # actively listen for messages until EXIT command
    while not isExit:
        message, clientAddress = serverSocketUDP.recvfrom(2048)
        clientMessage = message.decode()

        if clientMessage==exitCMD:
            isExit = True
        else:
            modifiedMessage = clientMessage[::-1]
            serverSocketUDP.sendto(modifiedMessage.encode(), clientAddress)

    # close the UDP connection 
    serverSocketUDP.close()
    print ("Successful Exit. UDP connection Closed")