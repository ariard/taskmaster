# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    launcher.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:57:06 by ariard            #+#    #+#              #
#    Updated: 2017/05/04 22:27:12 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys 
import time
import copy
import pty
import threading

from debug import *

import settings

def start_launcher(program, name_process, name_prog, retries):
    t = threading.Thread(target=launcher, args=(program, name_process, name_prog, retries))
    t.start()

def start_protected_launcher(program, name_process, name_prog, retries):
    t = threading.Thread(target=protected_launcher, args=(program, name_process, name_prog, retries))
    t.start()
    

class Process:
    def __init__(self, name_process, pid, status, retries, name_prog, master_fd):
        self.name_process = name_process
        self.pid = pid
        self.status = status
        self.retries = retries
        self.father = name_prog
        self.time = time.time()
        self.master = master_fd

def protected_launcher(program, name_process, name_prog, retries):
     
    while settings.tab_process[name_process].status != "EXITED" and settings.tab_process[name_process].status != "STOPPED" \
        and settings.tab_process[name_process].status != "FATAL":
        time.sleep(1)
    DG("ok " + name_process)
    launcher(program, name_process, name_prog, retries)

def launcher(program, name_process, name_prog, retries):

    try:
        pid, master_fd = pty.fork()
    except BlockingIOError:
        err_msg("Fork temporary unavailable") 

    if pid > 0:
        DG("new process : " + name_process)
        if program.startsecs > 0:
            status = "STARTING"
        elif program.startretries > retries:
            status = "BACKOFF"
        else:
            status = "RUNNING"
        process = Process(name_process, pid, status, retries, name_prog, master_fd)
        settings.pid2name[pid] = name_process
        settings.tab_process[name_process] = process
        settings.lst_pid.append(pid)
        time.sleep(2)
        os.write(master_fd, "hello world\r".encode("utf-8"))
        time.sleep(2)
        data = os.read(master_fd, 1024)
        fd = os.open(program.stdout, os.O_RDONLY)
        data = os.read(fd, 1024)
        DG(data.decode("utf-8"))

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
