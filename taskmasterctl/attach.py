# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    attach.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/04 18:07:37 by ariard            #+#    #+#              #
#    Updated: 2017/05/08 19:36:14 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import tty
import sys
import time
from select import select

from debug import *

STDIN_FILENO=0

def attach_mode(sc):

    DG("in attach mode")
    reply = sc.recv(1024)
    fd_client = os.open("/tmp/.client_attach", os.O_WRONLY)
    fd_server = os.open("/tmp/.server_attach", os.O_RDONLY)
    try:
        while True:
            line = input("\033[1;32m(attach mode)\033[0m ")
            timeout = 0 
            if len(line) == 0:
                timeout = time.time() + 2
            DG("gonna write { " + line + "}")
            os.write(fd_client, line.encode("utf-8"))
            DG("client : writing in client")
            if line == "detach":
                break
            fds = [fd_server]
            while True:
                rfds, wfds, xfds = select(fds, [], [])
                if fd_server in rfds:
                    data = os.read(fd_server, 1024)
#                    DG("back client gonna write {" + data.decode("utf-8") + "}")
                    if data:
                        os.write(sys.stdout.fileno(), data)
                        break
                if timeout != 0 and time.time() > timeout:
                    break
    except (OSError, ConnectionResetError) :
        pass
    print("Exiting attach mode")
