import socket
import threading

HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000  # Porta do servidor

# Cria um objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
s.connect((HOST, PORT))

# Função para receber mensagens do servidor
def receive_messages():
    while True:
        data = s.recv(1024)

        if not data:
            # Se não houver dados, a conexão foi encerrada
            break

        message = data.decode()
        print(message)


# Inicia uma nova thread para receber mensagens do servidor
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Aguarda uma entrada do usuário e envia mensagens para o servidor
while True:
    message = input('Digite uma mensagem: ')
    s.sendall(message.encode())
