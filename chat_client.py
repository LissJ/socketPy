# chat_client.py
import socket
import sys

def start_client():
    with open("config.txt", "r") as f:
        host, port = f.read().strip().split(":")
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, int(port)))
    print(f"Conectado ao servidor {host}:{port}")
    
    while True:
        msg = input("Cliente: ")
        client.send(msg.encode())
        if msg.lower() == "sair":
            break
        resposta = client.recv(1024).decode()
        print(f"Servidor: {resposta}")
    
    client.close()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "client":
        start_client()
