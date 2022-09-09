import socket
from threading import Thread

host = "127.0.0.1"
port_server = 12345
port_cliente = 12346

endereco_server = (host,port_server)

def recebe_msg(s: socket.socket):
    while True:
        msg_recebida, endereco = s.recvfrom(1024)

        print(f"Mensagem recebida: {msg_recebida.decode()}")

def envia_msg(s: socket.socket, endereco_server: tuple):
    while True:
        msg_digitada = input("Digite uma msg: ")
        s.sendto(msg_digitada.encode(), endereco_server)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((host,port_cliente))
    
    t1 = Thread(target=recebe_msg, args=(sock,))
    t2 = Thread(target=envia_msg, args=(sock,endereco_server))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()
