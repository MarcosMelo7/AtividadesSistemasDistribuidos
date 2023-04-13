import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

KEY = b'SuaChaveDeCriptografia'
HOST = ''
PORT = 5000

def decrypt(ciphertext):
    cipher = AES.new(KEY, AES.MODE_CBC, ciphertext[:16])
    return unpad(cipher.decrypt(ciphertext[16:]), AES.block_size)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor ouvindo em {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Conexão estabelecida por {addr}")
        while True:
            ciphertext = conn.recv(1024)
            if not ciphertext:
                break
            plaintext = decrypt(ciphertext)
            print(f"Mensagem recebida do cliente: {plaintext.decode()}")
            conn.sendall(ciphertext)  # envia mensagem criptografada de volta ao cliente
