import socket
import threading
import time

# Função para manipular uma conexão individual
def handle_client(connection):
    while True:
        data = connection.recv(1024)  # Recebe dados do cliente
        if not data:
            break  # Se não houver mais dados, encerra o loop

        # Processa os dados recebidos (nesse exemplo, apenas imprime na tela)
        print(f"Dados recebidos do cliente: {data.decode()}")

    # Adiciona uma carga de processamento adicional ao dormir por 1 segundo
    time.sleep(1)

    connection.close()  # Fecha a conexão

# Função principal do servidor
def start_server():
    host = 'localhost'
    port = 8888

    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Associa o socket ao host e à porta
    server_socket.bind((host, port))

    # Define o número máximo de conexões simultâneas
    server_socket.listen(5)

    print(f"Servidor escutando em {host}:{port}")

    while True:
        # Aguarda por novas conexões
        client_socket, client_address = server_socket.accept()
        print(f"Nova conexão de {client_address[0]}:{client_address[1]}")

        # Cria uma nova thread para tratar a conexão
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# Inicia o servidor
start_server()
