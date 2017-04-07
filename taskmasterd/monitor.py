# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    monitor.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 02:59:46 by ariard            #+#    #+#              #
#    Updated: 2017/04/07 04:27:10 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from execute import *

class monitor:
    def __init__(self, config, list_sections):
        self.config = config
        self.programs = list()
        self.programs.extend(list_sections)

    def launch(self):
        for i in self.programs:
            self.execute = execute(self.config, i)
            if self.execute.autostart == "true":
                while self.execute.numprocs > 1:
                    self.execute.set_command()
                    self.execute.exe_command()
                    self.execute.post_exe()
                    self.execute.numproc -= 1
                

                

