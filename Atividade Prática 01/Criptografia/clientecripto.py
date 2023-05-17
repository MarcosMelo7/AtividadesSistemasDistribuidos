import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

KEY = b'MinhaChaveDeCriptografia'
HOST = 'localhost'
PORT = 5000

def encrypt(plaintext):
    cipher = AES.new(KEY, AES.MODE_CBC)
    ciphertext = cipher.iv + cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def decrypt(ciphertext):
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    mensagem = b'Mensagem secreta'
    ciphertext = encrypt(mensagem)
    s.sendall(ciphertext)
    data = s.recv(1024)
    plaintext = decrypt(data)
    print(f"Resposta do servidor: {plaintext.decode()}")
