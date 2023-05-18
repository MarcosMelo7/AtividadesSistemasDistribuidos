import socket

HOST = 'localhost'  # define o host como localhost
PORT = 5000  # define a porta do servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    mensagem = "Hello World!!!"
    s.sendall(mensagem.encode())
    data = s.recv(1024)
    print(f"Mensagem invertida recebida do servidor: {data.decode()}")
