#!/bin/bash

# This program will ping all possible host connected on the network.

if [ "$1" == "" ]        # this is checking for the argument passed to the program
then                     # if the 1st argument is empty
echo "Usage: ./first_bash.sh [network]"
# this basically tells the user how to pass an argument to the program.
echo "example: ./first_bash.sh 192.168.20"
else              # if the argument is passed then, move ahead for the ping.
for x in $(seq 1 254); do

  # $1 takes the first argument passed in the program and appends with the value of x in the for loop.
ping -c 1 $1.$x       # actual ping message is sent.
done
fi  # end of if statement.