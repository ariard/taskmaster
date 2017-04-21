# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    server.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/06 23:56:10 by ariard            #+#    #+#              #
#    Updated: 2017/04/21 18:19:06 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import time
import socket
import threading

from debug import *

num_threads = 0

def new_client(clientsocket, addr):
    while True:
        m = clientsocket.recv(1024)
        m = m.strip()
        cmd_lst = m.split(' ')
        if not m:
            print('That motherfucking client ' + str(addr[1]) + ' sent a SIGINT signal, stopping...')
            break
        elif cmd_lst[0] == 'exit' or cmd_lst[0] == 'quit':
            print('exit request received from ' + str(addr[1]) + ' ... stopping')
            break
        elif cmd_lst[0] == 'start'
            
        print(addr, ' >> ', m)
        #m = raw_input('> ')
        #clientsocket.send(m + "\n")
    global num_threads
    num_threads -= 1
    print('debug: [' + str(num_threads) + '] threads are actually running')
    clientsocket.close()

class Server:
    def __init__(self, host, port):
        self.ss = socket.socket()
        self.host = host
        self.port = port
        self.c = None
        self.addr = None
        print("Server started and waiting for clients...")
        try:
            self.ss.bind((self.host, self.port))
        except:
            DG("port already bind")
            sys.exit(-1)
        self.ss.listen(5)

    def accept(self):
        DG("before accept")
        self.cs, self.sa = self.ss.accept()

    def receive(self):
        while True:
            data = self.cs.recv(1024)
            print(data)

     
#server.init #server.listen #server.deploy #server.exit
