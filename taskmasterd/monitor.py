# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    monitor.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 02:59:46 by ariard            #+#    #+#              #
#    Updated: 2017/04/13 00:37:52 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess
import os
import sys
import signal

from execute import *
from debug import *

# Table Prog
#   1 : command
#   2 : autostart
#   3 : autorestart
#   4 : startsecs
#   5 : startretries
#   6 : stopsignal
#   7 : stopwaitsecs
#   8 : stdout
#   9 : stderr
#   10: env
#   11: dir
#   12: umask
#   13: status

def check_exit(number, frame):
    while True:
        status = 0
        try:
            pid = os.waitpid(-1, 0)
        except:
            break
        print(pid[0])

class Monitor:
    def __init__(self, config, list_sections):
        self.config = config
        self.list_programs = list()
        self.list_programs.extend(list_sections)
        self.table_prog = dict()
        signal.signal(signal.SIGCHLD, check_exit)

    def launch_all(self):
        for i in self.list_programs:
            self.program = Program(self.config, i)
            if self.program.autostart == "true":
                while self.program.numprocs > 0:
                    self.launch(self.program, self.program.numprocs)
                    self.program.numprocs -= 1
        for i,j  in self.table_prog.items():
            print(i, j)
    
    def launch(self, program, numero):
        status = os.fork()
        self.table_prog[program.command + str(numero)] = [ program.command, \
            program.autostart, program.autorestart, program.startsecs, program.startretries, \
            program.stopsignal, program.stopwaitsecs, program.stdout, program.stderr, \
            program.env, program.dir, program.umask, status ]
        if status == 0:
            DG("launch command")
            program.conf()
            
#           log start
            try:
                args = program.command.split(' ')
                DG(args[0])
                os.execv(args[0], args)
            except:
                DG("log : no such program")
                sys.exit(-1)

