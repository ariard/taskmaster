# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    serviter.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:49:16 by ariard            #+#    #+#              #
#    Updated: 2017/04/29 23:19:06 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket

from debug import * 
from services import *

import settings

num_threads = 0

def serviter(clientsocket, addr, server):
    global num_threads

    retries = 3
    while retries > 0:
        answer = (clientsocket.recv(1024)).decode('utf-8')
        if answer == server.psswd:
            clientsocket.send(("valid").encode("utf-8"))
            retries = 0 
            services(clientsocket, addr, server)
        
        retries -= 1
        if retries == 0:
            clientsocket.send(("Too many false submits, deconnecting").encode("utf-8"))
            break
        elif retries > 0:
            clientsocket.send(("Wrong password, submit again").encode("utf-8"))

    num_threads -= 1
    DG('debug: [' + str(num_threads) + '] threads are actually running')
    clientsocket.close()
