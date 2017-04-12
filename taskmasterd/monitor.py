# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    monitor.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 02:59:46 by ariard            #+#    #+#              #
#    Updated: 2017/04/12 21:08:52 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess
import os
import sys

from execute import *
from debug import *

class Monitor:
    def __init__(self, config, list_sections):
        self.config = config
        self.list_programs = list()
        self.list_programs.extend(list_sections)
        self.table_prog = dict()

    def launch_all(self):
        for i in self.list_programs:
            self.program = Program(self.config, i)
            if self.program.autostart == "true":
                while self.program.numprocs > 0:
                    self.launch(self.program, self.program.numprocs)
                    self.program.numprocs -= 1
    
    def launch(self, program, numero):
        self.table_prog[program.command + str(numero)] = [ program.command, \
            program.autostart, program.autorestart, program.startsecs, program.startretries, \
            program.stopsignal, program.stopwaitsecs, program.stdout, program.stderr, \
            program.env, program.dir, program.umask ]
        status = os.fork()
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
