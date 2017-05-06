# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ioprocess.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/04 20:47:59 by ariard            #+#    #+#              #
#    Updated: 2017/05/06 20:41:45 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys
import pty
import tty
import time
from select import select

import settings
from debug import *

def unactive_ioprocess(process, clientsocket):

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


def _writen(fd, data):
    DG("my fd is " + str(fd))
    while data:
        n = os.write(fd, data)
        data = data[n:]

def _read(fd):
    return os.read(fd, 1024)

def ioprocess(process, clientsocket):

    master_fd = process.master
    clientsocket.send("synchro".encode('utf-8'))
    os.write(master_fd, "test again\r".encode("utf-8"))
    time.sleep(2)
    fd = os.open(settings.tab_prog[process.father].stdout, os.O_RDONLY)
    data = os.read(fd, 1024)
    DG(data.decode("utf-8"))
    fds = [fd]
    while True:
        reply = clientsocket.recv(1024)
        _writen(master_fd, reply)
        rfds, wfds, xfds = select(fds, [], [])
        if fd in rfds:
            data = _read(fd)
            DG(data.decode("utf-8"))
            if not data:
                fds.remove(fd)
            else:
                DG(data.decode("utf-8"))
#        if 1 in rfds:
#            data = _read(1)
#            if not data:
#                fds.remove(1)
#            else:
#                _writen(master_fd, data)
