# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 04:23:04 by ariard            #+#    #+#              #
#    Updated: 2017/04/11 19:12:54 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

class Program:
    def __init__(self, parse, program):
        if parse.get(program, "command"):
            self.command = parse.get(program, "command")
            self.numprocs = int(parse.get(program, "numprocs"))
            self.autostart = parse.get(program, "autostart")
            self.autorestart = parse.get(program, "autorestart")
            self.startsecs = parse.get(program, "startsecs")
            self.startretries = parse.get(program, "startretries")
            self.stopsignal = parse.get(program, "stopsignal")
            self.stopwaitsecs = parse.get(program, "stopwaitsecs")
            self.stdout = parse.get(program, "stdout_logfile")
            self.stderr = parse.get(program, "stderr_logfile")
            self.env = parse.get(program, "environnement")
            self.dir = parse.get(program, "directory")
            self.umask = parse.get(program, "umask")

    def conf(self):
        if self.dir == True:
            os.chdir(self.dir) 
        if self.umask == True:
            os.umask(self.umask)
#        for i, j in self.env:
#           os.environ[i] = j
        if self.stdout == True:
            fd = open(self.stdout, 'w+')
            os.dup2(fd, 1)
        if self.stderr == True:
            fd = open(self.stderr, 'w+')
            os.dup2(fd, 2)

