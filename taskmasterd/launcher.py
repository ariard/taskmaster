# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    launcher.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:57:06 by ariard            #+#    #+#              #
#    Updated: 2017/05/02 18:54:55 by ariard           ###   ########.fr        #
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

    try:
        pid = os.fork()
    except BlockingIOError:
        err_msg("Fork temporary unavailable") 

    if pid > 0:
        DG("new process with " + str(pid))
        if program.startsecs > 0:
            status = "STARTING"
        elif program.startretries > retries:
            status = "BACKOFF"
        else:
            status = "RUNNING"
        if settings.tab_prog[name_prog].numprocs > 1:
            name_process = name_prog[8:] + "_" + str(num)
        else:
            name_process = name_prog[8:]
        process = Process(name_process, pid, status, retries, num, name_prog)
        settings.pid2name[pid] = name_process
        settings.tab_process[name_process] = process
        settings.lst_pid.append(pid)

    if pid == 0:
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
