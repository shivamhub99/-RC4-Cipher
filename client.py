import socket
import os
from rc4 import rc4_encrypt

HOST = '127.0.0.1' 
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

message = input("Enter message to send to server: ")
length = len(message)

key = os.urandom(length)

encrypted_message = rc4_encrypt(key, message.encode())

client_socket.sendall(key)
client_socket.sendall(encrypted_message)

client_socket.close()
