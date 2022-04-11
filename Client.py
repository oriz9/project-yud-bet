import socket
import first_UI as ui
import select
import time
import threading
import hashlib
import os


class be_client:
    def __init__(self):
        self.client_socket = socket.socket()
        self.client_socket.connect(("127.0.0.1", 5555))


    def log_in(self):
        self.client_socket.send(("want connect").encode())
        ui.login_ui(self.client_socket)
        #is_log = False
        #self.client_socket.send(("want connect").encode())
        #data = self.client_socket.recv(1024).decode()
        #print(data)
        #while is_log == False:
         #   self.client_socket.send(str(input()).encode())
          #  data = self.client_socket.recv(1024).decode()
           # print(data)
           # if data == "well done u connect":
            #    is_log = True

    def tiksoret(self):
        # rlist, wlist, xlist = select.select([self.client_socket], [], [], 1)
        # data = self.client_socket.recv(1024).decode()
        # print("The server sent " + data)
        while True:
            # self.client_socket.send(self.the_message.encode())
            #self.client_socket.send(str(input()).encode())
            data = self.client_socket.recv(1024).decode()
            print(data)


if __name__ == '__main__':
    client = be_client()
    client.log_in()
    client.tiksoret()
