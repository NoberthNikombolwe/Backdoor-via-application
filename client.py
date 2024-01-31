# client.py
import socket
from connection_handler import connect_to_server

HOST = "192.168.252.146"
PORT = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect_to_server(client, (HOST, PORT))
