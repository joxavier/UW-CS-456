#!/bin/bash

#Script for sender application of 
#Assignment 2
#Computer Networks (CS 456 / CS 656)
#Number of parameters: 5
#Parameter:
#    $1: <host  address  of  the  network  emulator>
#    $2: <UDP  port  number  used  by  the  emulator  to receive data from the sender>
#    $3: <UDP port number used by the sender to receive ACKs from the emulator>
#    $4: <timeout interval in units of millisecond>
#    $5: <name of the file to be transferred>

#Uncomment exactly one of the following commands depending on your implementation

#For C/C++ implementation
#./client "$@"

#For Java implementation
#java client "$@"

#For Python implementation
python3 sender.py "$@"

#For Ruby implementation
#ruby client.rb "$@"