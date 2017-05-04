# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    attach.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/04 18:07:37 by ariard            #+#    #+#              #
#    Updated: 2017/05/04 21:49:45 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import tty

from debug import *

STDIN_FILENO=0

def attach_mode(sc):

    DG("in attach mode")
#    try:
#        mode = tty.tcgetattr(stdin_fileno)
#        tty.setraw(stdin_fileno)
#        restore = 1
#    except tty.error:
#        restore = 0
    sc.recv(1024)
    try:

        while True:
            line = input("\033[1;32m(attach mode)\033[0m ")
            sc.send(line.encode('utf-8'))
            if line == "detach":
                raise OSError
            
            while True:
                DG("waiting server answer")
                reply = sc.recv(1024).decode('utf-8')
                if len(reply) > 0 and reply != '\r':
                    print(reply.rstrip("\n\r"))
                if "\r" in reply:
                    break
    except (OSError, ConnectionResetError) :
        pass
#        if restore:
#            tty.tcsetattr(STDIN_FILENO, tty.TCSAFLUSH, mode)
    print("Exiting attach mode")
