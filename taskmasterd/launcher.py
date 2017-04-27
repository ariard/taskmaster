# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    launcher.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:57:06 by ariard            #+#    #+#              #
#    Updated: 2017/04/26 22:09:43 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys 
import time
import copy

from debug import *

import settings

class Process:
    def __init__(self, name_process, pid, status, retries, num, name_prog):
        self.name_process = name_process
        self.pid = pid
        self.status = status
        self.retries = retries
        self.num = num
        self.father = name_prog
        self.time = time.time()

def launcher(program, name_prog, num, retries):

    DG(name_prog)
    pid = os.fork()
    if pid > 0:
        if program.startsecs > 0:
            status = "STARTING"
        else:
            status = "RUNNING"
        name_process = name_prog[8:] + "_" + str(num)
        process = Process(name_process, pid, status, retries, num, name_prog)
        settings.pid2name[pid] = name_process
        settings.tab_process[name_process] = process
        settings.lst_pid.append(pid)

    if pid == 0:
        DG("launch command")
        program.conf()
        try:
            args = program.command.split(' ')
            DG(args[0])
#            log.update("[PROGRAM] - Launch " + str(program.command) + "\n")
#           log start + modify table_prog on shared memory
#            fifo = os.open("/tmp/fifo", os.O_WRONLY | os.O_SYNC)
            os.execv(args[0], args)
        except:
            DG("log : no such program")
            sys.exit(-1)
