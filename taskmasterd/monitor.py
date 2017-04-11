# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    monitor.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 02:59:46 by ariard            #+#    #+#              #
#    Updated: 2017/04/11 18:03:21 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess
import os

from execute import *
from table import *  

class Monitor:
    def __init__(self, config, list_sections):
        self.config = config
        self.list_programs = list()
        self.list_programs.extend(list_sections)
        self.tab_prog = tab_prog()

    def launch_all(self):
        for i in self.list_programs:
            self.program = program(self.config, i)
            if self.program.autostart == "true":
                while self.program.numprocs > 1:
                    self.launch(self)
                    self.program.numproc -= 1
    
    def launch(self):
        self.  
        status = os.fork()
        if status == 0:
            self.program.confv()
            subprocess.run(self.command)

    
