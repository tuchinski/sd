import socket
from threading import Thread

host = "127.0.0.1"
port = 12345
porta_cliente = 12346

endereco_server = (host, porta_cliente)

def recebe_msg(s: socket.socket):
    while True:
        msg_recebida, endereco = s.recvfrom(1024)

        print(f"Mensagem recebida: {msg_recebida.decode()}")

def envia_msg(s: socket.socket, endereco_server: tuple):
    while True:
        msg_digitada = input("Digite uma msg: ")
        s.sendto(msg_digitada.encode(), endereco_server)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((host,port))
    print("Server iniciado")

    t1 = Thread(target=recebe_msg, args=(s,))
    t2 = Thread(target=envia_msg, args=(s,endereco_server))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    

    while True:
        recebe_msg(s)
