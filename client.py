# this is socket programming for client

import socket

HOST = '192.168.1.4'
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send(f"Hello World!".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))
