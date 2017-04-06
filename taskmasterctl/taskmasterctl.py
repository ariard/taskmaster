# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __main__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/04 21:57:30 by ariard            #+#    #+#              #
#    Updated: 2017/04/06 23:49:49 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import os
import sys
import socket
import time

if __name__ == '__main__' :
        HOST = '127.0.0.1'
        PORT = 2121
        sys.stdout.write('>')
        sys.stdout.flush()
        sys.stdin.readline()
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, \
                        socket.getprotobyname("tcp"))
        client_socket.connect((HOST, PORT)) 
        client_socket.sendall(b'start')
        while True:
            sys.stdout.write('>')
            sys.stdout.flush()
            cmd = sys.stdin.readline()
            client_socket.sendall(str.encode(cmd))
