# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ioprocess.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/04 20:47:59 by ariard            #+#    #+#              #
#    Updated: 2017/05/04 22:25:25 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import pty
import tty
import time
from select import select

import settings
from debug import *

def ioprocess(process, clientsocket):

    try:
        fd = settings.tab_out[process.name_process]
    except KeyError:
        fd = os.open(settings.tab_prog[process.father].stdout, os.O_RDONLY)
        settings.tab_out[process.name_process] = fd
    DG("io process begin")
    clientsocket.send("synchro".encode('utf-8'))
    while True:
        DG("waiting client answer")
        data = clientsocket.recv(1024).decode('utf-8')
        if data == "detach":
            break
        while data:
            n = os.write(process.master, data.encode('utf-8'))
            data = data[n:]
        DG("writing to master")
        os.write(process.master, "\r".encode('utf-8'))
        time.sleep(1)
        data = os.read(fd, 1024)
        DG("data is " + str(data))
        DG("end of output") 
        clientsocket.send(data)
        clientsocket.send("\r".encode('utf-8'))
    DG("io process end")
