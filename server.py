# this is server side socket programming to establish an incoming connection from a client.

import socket

# we can also use "locahost" below.
HOST = '192.168.1.4'
# we don't use any of common port that are used by our system
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(HOST, PORT)

# server.listen(n) specifies upto how many connection our server will handle before leaving out any new
# incoming request.
server.listen(5)

while True:
    # server.accept() method is used to accept an incoming connection.
    communication_socket, address = server.accept()
    print(f"connected to {address}")
    # communication_socket.recv(n) --> here n defines number of bytes our server receives from the clint in msg.
    # this message is then decoded using utf-8, we can also choose ascii
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"message received from client is : {message}")
    communication_socket.send(f"received you message. Thank you!". encode('utf-8'))
    communication_socket.close()
    print(f"communication with {address} closed.")
