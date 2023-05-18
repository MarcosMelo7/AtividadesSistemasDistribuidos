import socket
import threading

# Função para enviar requisições ao servidor
def send_request():
    host = 'localhost'
    port = 8888
    message = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin dapibus elit a mi consectetur, vel posuere felis fermentum. Nullam commodo erat et mauris vehicula, vel ultricies sapien efficitur. Maecenas id justo vel justo bibendum lacinia. Nulla hendrerit finibus orci, nec malesuada turpis fringilla eu. Aliquam ut lectus eu sapien porttitor scelerisque. Quisque vestibulum libero at leo gravida, in tempus nulla mattis. Duis ullamcorper turpis et turpis volutpat, ac sollicitudin libero posuere. Nam ac pharetra velit.Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed id ipsum non justo tincidunt sollicitudin. Phasellus varius, nunc id tempor mattis, enim nisl placerat nunc, nec vestibulum nisl erat et libero. Donec fermentum semper diam, a malesuada sapien consequat sed. Nam ac tortor vel purus viverra interdum in sed ante. Fusce consectetur, magna vitae eleifend feugiat, quam nunc luctus ipsum, at iaculis enim arcu ac nisi. Aenean eget nisi ut dolor lobortis ullamcorper vel et mauris. Integer maximus lectus lacus, sed elementum elit convallis vitae. Vivamus eu tellus efficitur, tempor nulla vitae, fermentum sapien.Curabitur eleifend tristique volutpat. Mauris at libero finibus, molestie felis non, scelerisque velit. Maecenas iaculis urna eget turpis ullamcorper facilisis. Sed mollis dui in mi sagittis, sed consequat velit gravida. Nam aliquam nisi sit amet purus vulputate, sit amet bibendum odio lacinia. Donec elementum augue nec est finibus, eu luctus mi fermentum. Integer in tellus et diam auctor tempor nec vitae felis. Sed auctor feugiat purus, sed vestibulum ex consequat vel. Maecenas a lectus sed metus dictum finibus."

    while True:
        # Cria um socket TCP/IP
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conecta ao servidor
        client_socket.connect((host, port))

        # Envia a requisição
        client_socket.sendall(message)

        # Recebe a resposta do servidor
        data = client_socket.recv(1024)
        print(f"Resposta do servidor: {data.decode()}")

        # Fecha a conexão
        client_socket.close()

# Número de threads para enviar requisições simultâneas
num_threads = 1000000  

# Inicia várias threads para enviar requisições em massa ao servidor
for _ in range(num_threads):
    thread = threading.Thread(target=send_request)
    thread.start()

# Mantém o programa em execução para que as threads continuem enviando requisições
while True:
    pass
