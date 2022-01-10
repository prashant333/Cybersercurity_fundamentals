# this is the client side socket programming for server1

import socket

PORT = 9090
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '192.168.1.4'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


def send(msg):
    client.send(msg.encode(FORMAT))
    print(client.recv(1024).decode(FORMAT))


send("Hello World")
input("Enter your message: ")

send("Hello Everyone")
input()

send(DISCONNECT_MESSAGE)
