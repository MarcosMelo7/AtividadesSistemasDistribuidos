import socket
import threading

HOST = ''  # define o host como vazio para receber conexões de qualquer endereço
PORT = 5000  # define a porta do servidor
CLIENTS = []  # armazena as conexões de clientes

def client_thread(conn, addr):
    """
    Thread para cada cliente conectado.
    """
    print(f"Conexão estabelecida por {addr}")
    CLIENTS.append(conn)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        data = data.decode()
        reversed_data = data[::-1]  # inverte a ordem dos caracteres
        conn.sendall(reversed_data.encode())  # envia a mensagem de volta ao cliente

    print(f"Conexão fechada com {addr}")
    CLIENTS.remove(conn)
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor ouvindo em {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        threading.Thread(target=client_thread, args=(conn, addr)).start()
