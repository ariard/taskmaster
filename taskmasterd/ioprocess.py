# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ioprocess.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/04 20:47:59 by ariard            #+#    #+#              #
#    Updated: 2017/05/07 00:13:17 by ariard           ###   ########.fr        #
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

def writen(fd, data):
    while data:
        n = os.write(fd, data)
        data = data[n:]

def ioprocess(process, clientsocket):

    master_fd = process.master
    try:
        os.unlink("/tmp/.out_attach")
        os.unlink("/tmp/.in_attach")
    except FileNotFoundError:
        pass 
    out = os.open("/tmp/.out_attach", os.O_CREAT | os.O_RDONLY)
    infd = os.open("/tmp/.in_attach", os.O_CREAT | os.O_WRONLY)
    clientsocket.send("synchro".encode('utf-8'))
    fd = os.open(settings.tab_prog[process.father].stdout, os.O_RDONLY)
    fds = [fd, out]
    while True:
        rfds, wfds, xfds = select(fds, [], [])
        if fd in rfds:
            data = os.read(fd, 1024)
            DG(data.decode("utf-8"))
            if data:
                writen(infd, data + "\r".encode("utf-8"))
        if out in rfds:
            data = os.read(out, 1024) 
            if data:
                writen(master_fd, data + "\r".encode("utf-8"))
