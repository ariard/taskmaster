# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    attach.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/04 18:07:37 by ariard            #+#    #+#              #
#    Updated: 2017/05/11 23:08:42 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import tty
import sys
import time
from select import select

from taskmaster.debug import *

def writen(fd, data):
    while data:
        n = os.write(fd, data)
        data = data[n:]

def attach_mode(sc):

    DG("in attach mode")
    print("Attach mode initialization")
    reply = sc.recv(1024)
    if reply.decode("utf-8") == "detach":
        print ("A client is already in attach mode")
        return 1 
    fd_client = os.open("/tmp/.client_attach", os.O_WRONLY)
    fd_server = os.open("/tmp/.server_attach", os.O_RDONLY)
    try:
        while True:
            line = input("\033[1;32m(attach mode)\033[0m ")
            timeout = 0 
      #     if len(line) == 0:
            timeout = time.time() + 2
            writen(fd_client, line.encode("utf-8"))
            if line == "detach":
                break
            if line == "detach2":
                print("Process should be running to be in attach mode")
                break
            fds = [fd_server]
            while True:
                rfds, wfds, xfds = select(fds, [], [])
                if fd_server in rfds:
                    DG("before read")
                    data = os.read(fd_server, 1024)
                    DG("after read")
                    if data:
                        DG("got data")
                        os.write(sys.stdout.fileno(), data)
                        timeout = 0
                        break
                DG("len is " + str(len(line)))
                DG("timeout" + str(timeout))
                DG("time" + str(time.time()))
                if timeout != 0 and time.time() > timeout:
                    break
    except (OSError, ConnectionResetError) :
        pass
    print("Exiting attach mode")
