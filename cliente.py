import socket
from threading import Thread

HOST = "127.0.0.1"  
PORT = 65431

def escuta_server(s):
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(f"Recebi o dado {data.decode()}")

def envia_server(s):
    while True:
        dado_para_enviar = input()
        if dado_para_enviar.upper() == 'SAIR':
            break
        
        s.sendall(dado_para_enviar.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) # conecta com o server

    t1 = Thread(target=escuta_server, args=(s,))
    t2 = Thread(target=envia_server, args=(s,))
    
    t1.start()
    t2.start()

    # t1.join()
    t2.join()
    exit()

    # s.sendall(b"Hello, world")
    # data = s.recv(1024)

# print(f"Received {data!r}")
