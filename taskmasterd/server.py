# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    server.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/06 23:56:10 by ariard            #+#    #+#              #
#    Updated: 2017/04/06 23:56:53 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import time
import socket

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

#server.init #server.listen #server.deploy #server.exit
