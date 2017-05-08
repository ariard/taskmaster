# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ioprocess.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/04 20:47:59 by ariard            #+#    #+#              #
#    Updated: 2017/05/08 20:41:04 by ariard           ###   ########.fr        #
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

def remove_tmp_fd(out, err):
    pos = settings.fds.index(out)
    settings.fds.pop(pos)
    pos = settings.fds.index(err)
    settings.fds.pop(pos)

def writen(fd, data):
    while data:
        n = os.write(fd, data)
        data = data[n:]

def ioprocess(process, clientsocket):

    DG("begin of ioprocess with " + process.name_process)
    try:
        os.unlink("/tmp/.client_attach")
        os.unlink("/tmp/.server_attach")
    except FileNotFoundError:
        pass
    fd_client = os.open("/tmp/.client_attach", os.O_CREAT | os.O_RDONLY)
    fd_server = os.open("/tmp/.server_attach", os.O_CREAT | os.O_WRONLY)
    clientsocket.send("synchro".encode('utf-8'))
    in_process = process.process_fd[0] 
    out_process = process.process_fd[1] 
    err_process = process.process_fd[2] 
    
    remove_tmp_fd(out_process, err_process)
    DG("settings is : " + str(settings.fds))

    while True:

        fds = [fd_client, out_process, err_process] 

        rfds, wfds, xfds = select(fds, [], [])

        if fd_client in rfds:
            data = os.read(fd_client, 1024)
            if data.decode("utf-8") == "detach":
                break
            if data:
                DG("server : writing in process")
                data = data.decode("utf-8")
                os.write(in_process, data.encode("utf-8") + "\n".encode("utf-8"))

        if out_process in rfds:
            data = os.read(out_process, 1024)
            if data:
                DG("server : writing in server")
                DG("server back write {" + data.decode("utf-8") + "}")
                data = data.decode("utf-8")
                os.write(fd_server, data.encode("utf-8"))

        if err_process in rfds:
            data = os.read(err_process, 1024)
            if data:
                DG("server : writing in server")
                DG("server back write {" + data.decode("utf-8") + "}")
                writen(fd_server, data)
    settings.fds.append(out_process)
    settings.fds.append(err_process)
    os.close(fd_client)
    os.close(fd_server)
    DG("end of ioprocess")
