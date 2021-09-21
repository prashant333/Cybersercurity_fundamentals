#!/usr/bin/python
""" Please make sure that the python is installed at the above given PATH, else change the above line to specific
location where python is installed."""

import socket
ip = raw_input("Enter the IP: ")
port = input("Enter the port: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s.connect_ex((ip, port)):
    print "Port", port, "is closed"
else:
    print "Port", port, "is open"