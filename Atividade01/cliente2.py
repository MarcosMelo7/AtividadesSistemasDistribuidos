import socket

HOST = 'localhost'  # define o host como localhost, ou seja, a máquina local
PORT = 5000  # define a porta do servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Voces estao bem?')
    data = s.recv(1024)

print(f"Resposta do servidor: {data.decode()}")
