import socket
from rc4 import rc4_decrypt

HOST = '127.0.0.1' 
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen()

print('Server listening on {}:{}'.format(HOST, PORT))

client_socket, client_address = server_socket.accept()
print('Connected by', client_address)

key = client_socket.recv(1024)

strkey = str(key)

data = client_socket.recv(1024)
print("The shared key is ",strkey)
try:
    decrypted_data = rc4_decrypt(key, data)
    print('Decrypted message:', decrypted_data.decode('utf-8', 'ignore'))
except UnicodeDecodeError:
    print('Decryption Error: Cannot decode decrypted data as UTF-8')

client_socket.close()
server_socket.close()

