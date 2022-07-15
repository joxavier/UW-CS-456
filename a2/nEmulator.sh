#!/bin/bash

#Script for receiver application of
#Assignment 2
#Computer Networks (CS 456)
#Number of parameters: 4
#Parameter:
#    $1: <name  of  the  file  into  which  the received data is written>
#    $2: <receiver's network address>
#    $3: <receiver's receiving UDP port number>
#    $4: <emulator's receiving UDP port number in the backward (receiver) direction>
#    $5: <sender's network address>
#    $6: <sender's receiving UDP port number>
#    $7: <maximum delay of the link in units of millisecond>
#    $8: <packet discard probability>
#    $9: <verbose-mode>

#For Python implementation
if [ "$#" -ne 9 ];
then
  echo "Error: Program takes 9 parameters"
  exit 1
fi

python3 network_emulator.py $1 $2 $3 $4 $5 $6 $7 $8 $9