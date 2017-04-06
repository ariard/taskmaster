# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __main__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/04 21:57:30 by ariard            #+#    #+#              #
#    Updated: 2017/04/06 23:57:07 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import os
import sys
import signal
import time
import socket
from daemonize import *
from server import *


def server():
# Change HOST value    
    HOST = ''
    PORT = 2121
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, \
                    socket.getprotobyname("tcp"))
    if server_socket.bind((HOST, PORT)) == False:
        sys.exit(-1)
    server_socket.listen(42)
    client_socket, client_addr = server_socket.accept()
    while True:
        data = client_socket.recv(1024)
        if data:
            print("Received", repr(data))
        else:
            time.sleep(1)


if __name__ == '__main__' :
    daemonize()
    server()


#server.init #server.listen #server.deploy #server.exit
