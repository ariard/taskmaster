# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reporter.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:45:20 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 17:33:31 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

from debug import *

def watcher():
    global table_prog
    global table_process 

    while 1:
        fifo = open("/tmp/fifo", "r")
        for line in fifo:
            startinfos = line.split(";")
            if table_process[startinfos[0]][1] == "STARTING":
                table_process[startinfos[0]] += startinfos[1]
        fifo.close()

    #TO IMPLEMENT, THREAD DEDIE POUR UDPDATE DATE DES PROCESS
