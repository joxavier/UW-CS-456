#!/bin/bash

#Script for receiver application of
#Assignment 2
#Computer Networks (CS 456)
#Number of parameters: 4
#Parameter:
#    $1: <hostname for the network emulator>
#    $2: <UDP port number used by the link emulator to receive ACKs from the receiver>
#    $3: <UDP port number used by the receiver  to  receive  data  from  the  emulator>
#    $4: <name  of  the  file  into  which  the received data is written>

#For Python implementation
if [ "$#" -ne 4 ];
then
  echo "Program takes 4 parameters, <hostname for the network emulator>, <UDP port number used by the link emulator to receive ACKs from the receiver>, <UDP port number used by the receiver  to  receive  data  from  the  emulator>, and <name  of  the  file  into  which  the received data is written>"
  exit 1
fi

python3 reciever.py $1 $2 $3 $4