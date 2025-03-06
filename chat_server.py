# chat_server.py
import socket
import sys

def start_server():
    with open("config.txt", "r") as f:
        host, port = f.read().strip().split(":")
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, int(port)))
    server.listen(1)
    print(f"Servidor rodando em {host}:{port}")
    
    conn, addr = server.accept()
    print(f"Conectado a {addr}")
    
    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == "sair":
            break
        print(f"Cliente: {data}")
        resposta = input("Servidor: ")
        conn.send(resposta.encode())
    
    conn.close()
    server.close()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "server":
        start_server()
