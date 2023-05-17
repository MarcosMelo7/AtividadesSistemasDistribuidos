import socket
import threading

HOST = ''  # Endereço IP do servidor
PORT = 5000  # Porta que o servidor vai escutar

# Lista para armazenar todas as conexões de clientes
connections = []

# Cria um objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o objeto socket ao endereço e porta especificados
s.bind((HOST, PORT))

# Define o limite máximo de conexões simultâneas
s.listen(5)

print(f'Servidor escutando na porta {PORT}...')


def handle_client_connection(conn, addr):
    # Envia uma mensagem de boas-vindas para o cliente conectado
    conn.sendall('Bem-vindo ao chat!'.encode())

    while True:
        try:
            # Aguarda uma mensagem do cliente
            data = conn.recv(1024)

            if not data:
                # Se não houver dados, a conexão foi encerrada
                break

            message = data.decode()

            # Encaminha a mensagem para todos os outros clientes conectados
            for client_conn in connections:
                if client_conn != conn:
                    client_conn.sendall(message.encode())

        except ConnectionResetError:
            # Se a conexão for redefinida, desconecta o cliente
            break

    # Remove a conexão do cliente da lista de conexões
    connections.remove(conn)
    conn.close()


while True:
    # Aguarda uma conexão
    conn, addr = s.accept()
    print(f'Conectado por {addr}')

    # Adiciona a conexão do cliente à lista de conexões
    connections.append(conn)

    # Inicia uma nova thread para lidar com a conexão do cliente
    thread = threading.Thread(target=handle_client_connection, args=(conn, addr))
    thread.start()
