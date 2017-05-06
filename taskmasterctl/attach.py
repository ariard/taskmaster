# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    attach.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/04 18:07:37 by ariard            #+#    #+#              #
#    Updated: 2017/05/06 23:21:33 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import tty

from debug import *

STDIN_FILENO=0

def attach_mode(sc):

    DG("in attach mode")
    sc.recv(1024)
    try:

        while True:
            line = input("\033[1;32m(attach mode)\033[0m ")
            DG("line is [" + line + "]")
#            if len(line) == 0:
#                DG("continue")
#                continue
#            sc.send(line.encode('utf-8'))
            if line == "detach":
                raise OSError
            
            while True:
                DG("waiting server answer")
                reply = sc.recv(1024).decode('utf-8')
                DG("after server callback")
                DG("das reply is " + reply)
                if len(reply) > 0 and reply != '\r':
                    print(reply.rstrip("\n\r"))
                if "\r" in reply:
                    break
    except (OSError, ConnectionResetError) :
        pass
    print("Exiting attach mode")
