# server.py
import socket
from connection_handler import accept_connections

HOST = "192.168.252.146"
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

accept_connections(server)
