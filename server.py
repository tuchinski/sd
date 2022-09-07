import socket
from threading import Thread
import sys

HOST = "127.0.0.1"
PORT = 65431

def escuta_client(s):
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(f"Recebi o dado {data.decode()}")

def envia_cliente(s):
    while True:
        dado_para_enviar = input()
        if dado_para_enviar.upper() == 'SAIR':
            sys.exit()
            break
        
        s.sendall(dado_para_enviar.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept() # cria e configura o server

    with conn:
        print(f"Connected by {addr}")
        while True:
            # data = conn.recv(1024)
            # print(f"Server recebeu o dado {data}")
            # if not data:
                # break
            t1 = Thread(target=escuta_client, args=(conn,))
            t2 = Thread(target=envia_cliente, args=(conn,))
            t1.start()
            t2.start()

            t2.join()
            
