# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reporter.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:45:20 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 19:44:48 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

from debug import *

import settings

def watcher():
    table_prog = settings.table_prog
    table_process = settings.table_process

    while 1:
        try:
            fifo = open("/tmp/fifo", "r")

            for line in fifo:
                startinfos = line.split(";")

                if table_process[startinfos[0]][1] == "STARTING":
                    table_process[startinfos[0]] += startinfos[1]
                fifo.close()
        except:
            pass
    #TO IMPLEMENT, THREAD DEDIE POUR UDPDATE DATE DES PROCESS
