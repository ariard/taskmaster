# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    launcher.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:57:06 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 19:50:32 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys 
import time
import copy

from debug import *

import settings

def launcher(program, name_prog):
    table_prog = settings.table_prog
    table_process = settings.table_process
    prog_to_pid = settings.prog_to_pid

    pid = os.fork()
    if pid > 0:
        if program.startsecs == 0:
            status = "STARTING"
        else:
            status = "RUNNING"
        table_process[pid] = [name_prog, status, copy.copy(program.startretries)]
        prog_to_pid[name_prog] = None

    if pid == 0:
        DG("launch command")
        program.conf()
        try:
            args = program.command.split(' ')
            DG(args[0])
#            log.update("[PROGRAM] - Launch " + str(program.command) + "\n")
#           log start + modify table_prog on shared memory
#            fifo = os.open("/tmp/fifo", os.O_WRONLY | os.O_SYNC)
            fifo = open("/tmp/fifo", "w")
            fifo.write(str(os.getpid()) + ";" + str(time.time()) + "\n")
#            os.close(fifo)
            fifo.close()
            DG("after write FIFO")
            os.execv(args[0], args)
        except:
            DG("log : no such program")
            sys.exit(-1)
