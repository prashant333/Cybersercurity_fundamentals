# this is server side socket programming with multi threading.

import socket
import threading

HOST = '192.168.1.4'
PORT = 9090
FORMAT = 'utf-8'
DISCONNECTED_MESSAGE = '!DISCONNECTED'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


def handle_client(conn, addr):
    print(f"[NEW CONNECTION]{addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(1024).decode(FORMAT)
        if msg == DISCONNECTED_MESSAGE:
            connected = False

        print(f"[{addr}] {msg}")
        conn.send(f"Message received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] server is listing on {HOST}")
    while True:
        conn, add = server.accept()
        thread = threading.Thread(target=handle_client(), args=(conn, add))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count()-1}")


print("[STARTING] server is listing...")
start()

