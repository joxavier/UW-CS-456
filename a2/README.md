# S22 - CS 456 Assignment 2: A congestion controlled pipelined RDT
# Joshua Xavier

## How to run the program
chmod +x ./nEmulator.sh
chmod +x ./reciever.sh
chmod +x ./sender.sh
./nEmulator.sh <emulator's receiving UDP port number in the forward (sender) direction>,
<receiver's network address>,
<receiver's receiving UDP port number>,
<emulator's receiving UDP port number in the backward (receiver) direction>,
<sender's network address>,
<sender's receiving UDP port number>,
<maximum delay of the link in units of millisecond>,
<packet discard probability>,
<verbose-mode>

./reciever.sh <hostname for the network emulator>,
<UDP port number used by the link emulator to receive ACKs from the receiver>,
<UDP port number used by the receiver to receive data from the emulator>,
<name of the file into which the received data is written>

./sender.sh <host address of the network emulator>,
<UDP port number used by the emulator to receive data from the sender>,
<UDP port number used by the sender to receive ACKs from the emulator>,
<timeout interval in units of millisecond>,
<name of the file to be transferred>

## sample parameters
./nEmulator.sh 9991 10.15.154.52 9994 9993  10.15.154.27 9992 1 0.2 1
./reciever.sh 10.15.154.51 9993 9994 out.txt
./sender.sh 10.15.154.51 9991 9992 50 sendfile.txt

## Undergrad machines your program was built and tested on
ubuntu2004.student.cs.uwaterloo.ca
ubuntu2004-002.student.cs.uwaterloo.ca
ubuntu2004-004.student.cs.uwaterloo.ca

## Version of make and compilers
Python 3.9.13