# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ioprocess.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/04 20:47:59 by ariard            #+#    #+#              #
#    Updated: 2017/05/06 23:48:18 by ariard           ###   ########.fr        #
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

def writen(fd, data):
    DG("my fd is " + str(fd))
    while data:
        n = os.write(fd, data)
        data = data[n:]

def ioprocess(process, clientsocket):

    master_fd = process.master
    try:
        os.unlink("/tmp/.out_attach")
    except FileNotFoundError:
        pass 
    out = os.open("/tmp/.out_attach", os.O_CREAT | os.O_RDONLY)
    clientsocket.send("synchro".encode('utf-8'))
    fd = os.open(settings.tab_prog[process.father].stdout, os.O_RDONLY)
    fds = [fd, out]
    while True:
        rfds, wfds, xfds = select(fds, [], [])
#        DG("MASTER select")
        if fd in rfds:
            data = os.read(fd, 1024)
            DG(data.decode("utf-8"))
            if data:
                clientsocket.send(data)
                clientsocket.send("\r".encode("utf-8"))
#                break
        if out in rfds:
            data = os.read(out, 1024) 
            if data:
                writen(master_fd, data + "\r".encode("utf-8"))
#    clientsocket.send("\r".encode("utf-8"))
