# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    server.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/06 23:56:10 by ariard            #+#    #+#              #
#    Updated: 2017/04/13 15:21:26 by ataguiro         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import time
import socket

from debug import *

class Server:
    def __init__(self, host, port):
        DG("server init")
        self.host = host
        self.port = port
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, \
                        socket.getprotobyname("tcp"))
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
