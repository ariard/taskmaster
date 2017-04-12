# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 04:23:04 by ariard            #+#    #+#              #
#    Updated: 2017/04/12 22:19:32 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

from debug import *

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
        DG(" conf") 
        try:
            DG(self.dir)
            os.chdir(self.dir) 
        except:
            DG("log : couldn't chdir")
        try:
            os.umask(int(self.umask))
        except:
            DG("log : couldn't umask")
        try:
            list_env = self.env.split(',')
            for i in list_env:
                j = i.split('=')
                os.environ[j[0]] = j[1]
        except:
            DG("log : couldn't set env")
        try:
            fd = open(self.stdout, 'w+')
            os.dup2(fd.fileno(), 1)
        except:
            DG("log : couldn't set stdout")
        try:
            fd = open(self.stderr, 'w+')
            os.dup2(fd.fileno(), 2)
        except:
            DG("log : couldn't set stderr")
