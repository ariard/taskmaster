# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    monitor.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 02:59:46 by ariard            #+#    #+#              #
#    Updated: 2017/04/14 18:50:06 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess
import os
import sys
import signal

from execute import *
from debug import *

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

def launch(program):
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
            os.execv(args[0], args)
        except:
            DG("log : no such program")
            sys.exit(-1)

def check_exit(number, frame):
    while True:
        status = 0
        try:
            pid = os.waitpid(-1, 0)
            program = table_prog[pid[0]]
            if program[3] != pid[1] \
            and program[2] == "true":
                if program[5] > 0:
                    program[13].startretries -= 1
                    launch(program[13])
        except:
            break


class Monitor:
    def __init__(self, config, list_sections):
        self.config = config
        self.list_programs = list()
        self.list_programs.extend(list_sections)
        signal.signal(signal.SIGCHLD, check_exit)

    def launch_all(self):
        for i in self.list_programs:
            self.program = Program(self.config, i)
            if self.program.autostart == "true":
                while self.program.numprocs > 0:
                    launch(self.program)
                    self.program.numprocs -= 1
#        for i,j  in table_prog.items():
#            print(i, j)
