import hashlib
import socket
import select
import pickle
import Mongodb_A
from time import sleep

class my_server:
    MAX_MSG_LENGTH = 1024
    port = 5555
    ip = "127.0.0.1"

    def __init__(self):
        self.to_send = ""
        # network variables:
        self.server_socket = socket.socket()
        self.client_sockets = []

    def init_network(self):
        self.server_socket.bind((my_server.ip, my_server.port))
        self.server_socket.listen()
        print("Listening for clients...")

    def log_in_account(self, current_socket):
        right_name = False
        right_pas = False
        current_socket.send((str("what your name?")).encode())
        while right_name == False:
            data = current_socket.recv(my_server.MAX_MSG_LENGTH).decode()
            password_account = Mongodb_A.getPasw_name(data)
            print("123")
            print(password_account)
            if password_account == "":
                current_socket.send((str("bad name try again")).encode())
            else:
                right_name = True
        current_socket.send((str("password")).encode())
        data = current_socket.recv(my_server.MAX_MSG_LENGTH).decode()
        while right_pas == False:
            if data == password_account:
                current_socket.send(("well done u connect").encode())
                right_pas = True
            else:
                current_socket.send(("wrong password please try again").encode())
            data = current_socket.recv(my_server.MAX_MSG_LENGTH).decode()

    def do_iteration(self):
        messsage_to_send = []
        rlist, wlist, xlist = select.select([self.server_socket] + self.client_sockets, self.client_sockets, [])
        for current_socket in rlist:
            if current_socket is self.server_socket:
                connection, client_address = current_socket.accept()
                print("New client joined!", client_address)
                self.client_sockets.append(connection)
                print_client_sockets(self.client_sockets)
            else:
                data = current_socket.recv(my_server.MAX_MSG_LENGTH).decode()
                print(data)
                if data == "want connect":
                    self.log_in_account(current_socket)
                elif data == "":
                    print("Connection closed", )
                    self.client_sockets.remove(current_socket)
                    current_socket.close()
                    print_client_sockets(self.client_sockets)
                else:
                    messsage_to_send.append((current_socket, data))

        for message in messsage_to_send:
            current_socket, data = message
            if current_socket in wlist:
                current_socket.send(data.encode())
                messsage_to_send.remove(message)

def print_client_sockets(client_sockets):
    for c in client_sockets:
        print("\t", c.getpeername())

def main():
    server = my_server()
    server.init_network()

    while True:
        server.do_iteration()

if __name__ == '__main__':
    main()