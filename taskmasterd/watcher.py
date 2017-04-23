# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reporter.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:45:20 by ariard            #+#    #+#              #
#    Updated: 2017/04/23 18:16:22 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

from debug import *

import settings

def watcher():

    while 1:
        try:
            fifo = open("/tmp/fifo", "r")

            for line in fifo:
                startinfos = line.split(";")

                if settings.tab_process[startinfos[0]][1] == "STARTING":
                    tab_process[startinfos[0]] += startinfos[1]
                fifo.close()
        except:
            pass
    #TO IMPLEMENT, THREAD DEDIE POUR UDPDATE DATE DES PROCESS
