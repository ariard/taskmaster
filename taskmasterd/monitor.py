# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    monitor.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 02:59:46 by ariard            #+#    #+#              #
#    Updated: 2017/04/21 20:58:23 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess
import os
import sys
import signal
import threading

from execute import *
from debug import *

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
                numprocs = self.programs.numprocs
                while self.program.numprocs > 0:
                    launcher(self.program, numprocs)
                    self.program.numprocs -= 1
#        for i,j  in table_prog.items():
#            print(i, j)

    def start_guardian(self):
        t = threading.Thread(target=guardian)
        t.start()

    def start_reporter(self):
        t = threading.Thread(target=reporter)
        t.start()
    
    def start_killer(self, program):
        t = threading.Thread(target=killer, args=program)
        t.start()

    def start_configurator(self): 
        t = threading.Thread(target=configurator, args=(monitor))
        t.start()
