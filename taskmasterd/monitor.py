# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    monitor.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 02:59:46 by ariard            #+#    #+#              #
#    Updated: 2017/04/12 16:15:40 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess
import os

from execute import *

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
                while self.program.numprocs > 1:
                    self.launch(self, self.program, self.program)
                    self.program.numproc -= 1
    
    def launch(self, program, numero):
        self.table_prog[program.command + str(numero)] = [ self.command, \
            self.autostart, self.autorestart, self.startsecs, self.startretries, \
            self.stopsignal, self.stopwaitsecs, self.stdout, self.stderr, \
            self.env, self.dir, self.umask ]
        status = os.fork()
        if status == 0:
            program.conf()
#           log start    
            subprocess.run(program.command)
