# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    attach.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/04 18:07:37 by ariard            #+#    #+#              #
#    Updated: 2017/05/07 00:17:12 by ariard           ###   ########.fr        #
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
    if reply == "detach":
        sys.stderr.write("taskmasterd: No such process")
    out = os.open("/tmp/.out_attach", os.O_WRONLY)
    infd = os.open("/tmp/.in_attach", os.O_RDONLY)
    try:
        while True:
            line = input("\033[1;32m(attach mode)\033[0m ")
            timeout = 0 
            if len(line) == 0:
                timeout = time.time() + 2
            os.write(out, line.encode("utf-8"))
            if line == "detach":
                raise OSError
            fds = [infd]
            while True:
                rfds, wfds, xfds = select(fds, [], [])
                if infd in rfds:
                    data = os.read(infd, 1024)
                    if data:
                        print(data.decode("utf-8").rstrip("\n\r"))
                        break
                if timeout != 0 and time.time() > timeout:
                    break
    except (OSError, ConnectionResetError) :
        pass
    print("Exiting attach mode")
