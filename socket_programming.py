# An example script to connect to Google using socket
# programming in Python

import socket # for socket
import sys

try:
	# socket.AF_INET --> specifies that this is an internet socket,
	# socket.SOCK_STREAM --> specifies that this is an TCP connection
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket successfully created")
except socket.error as err:
	print("socket creation failed with error %s" %(err))

# default port for socket
port = 80

try:
	# host_ip = socket.gethostbyname(socket.gethostname()) --> this command will automatically retrieve the
	# ip address of the running computer.
	host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:

	# this means could not resolve the host
	print("there was an error resolving the host")
	sys.exit()

# connecting to the server
s.connect((host_ip, port))

print("the socket has successfully connected to google")
