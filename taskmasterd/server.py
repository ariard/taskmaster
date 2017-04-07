# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    server.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/06 23:56:10 by ariard            #+#    #+#              #
#    Updated: 2017/04/07 00:35:09 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import time
import socket

class server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, \
                        socket.getprotobyname("tcp"))
        if self.ss.bind((self.host, self.port)) == False:
             sys.exit(-1)
        self.ss.listen(42)

    def accept(self):
        self.cs, self.sa = self.ss.accept()

    def receive(self):
        while True:
            data = self.cs.recv(1024)

#server.init #server.listen #server.deploy #server.exit
