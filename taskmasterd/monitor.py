# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    monitor.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 02:59:46 by ariard            #+#    #+#              #
#    Updated: 2017/04/18 19:21:42 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess
import os
import sys
import signal
import threading
import time

from execute import *
from debug import *
from task_signal import *

# Table Prog
#   0 : command
#   1 : autostart
#   2 : autorestart
#   3 : exitcodes
#   4 : startsecs
#   5 : startretries
#   6 : stopsignal
#   7 : stopwaitsecs
#   8 : stdout
#   9 : stderr
#   10: env
#   11: dir
#   12: umask
#   13 : program

table_prog = dict()

def launcher(program):
    global table_prog

    status = os.fork()
    table_prog[status] = [ program.command, \
        program.autostart, program.autorestart, program.exitcodes, \
        program.startsecs, program.startretries, program.stopsignal, \
        program.stopwaitsecs, program.stdout, program.stderr, \
        program.env, program.dir, program.umask, program, program.status]

    if status == 0:
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

def guardian():
    global queue_pid
    global table_lock

    while 1 :
        while len(queue_pid) > 1:
            pid = queue_pid[0]
            status = queue_pid[1]
            program = table_prog[pid]
            if program[3] != status and program[2] == "true":
                if program[5] > 0:
                    program[13].startretries -= 1
                    launcher(program[13])
            queue_pid.pop(0)
            queue_pid.pop(0) 
        time.sleep(1)

def reporter():
    while 1:
        fifo = open("/tmp/fifo", "r")
        for line in fifo:
            starter = line.split(";")
#           DG("starter :" + line)
        fifo.close()

class Monitor:
    def __init__(self, config, list_sections):
        self.config = config
        self.list_programs = list()
        self.list_programs.extend(list_sections)
        signal.signal(signal.SIGCHLD, check_exit)
        try:
            os.mkfifo("/tmp/fifo", mode=0o666)
        except:
            DG("log : fifo already exist")

    def launch_all(self):
        for i in self.list_programs:
            self.program = Program(self.config, i)
            if self.program.autostart == "true":
                while self.program.numprocs > 0:
                    launcher(self.program)
                    self.program.numprocs -= 1
#        for i,j  in table_prog.items():
#            print(i, j)

    def start_guardian(self):
        t = threading.Thread(target=guardian)
        t.start()

    def start_reporter(self):
        t = threading.Thread(target=reporter)
        t.start()
