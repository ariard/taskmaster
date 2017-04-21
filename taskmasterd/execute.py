# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 04:23:04 by ariard            #+#    #+#              #
#    Updated: 2017/04/21 23:29:53 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

from debug import *

class Program:
    def __init__(self, config , name_prog):
            try:
                self.command = config.get(name_prog, "command")
            except configparser.ParsingError:
                self.command = ""
            try:
                self.numprocs = int(config.get(name_prog, "numprocs"))
            except configparser.ParsingError:
                self.numprocs = 1
            try:
                self.autostart = config.get(name_prog, "autostart")
            except configparser.ParsingError:
                self.autostart = "true"
            try:
                self.autorestart = config.get(name_prog, "autorestart")
            except configparser.ParsingError:
                self.autorestart = "unexpected" 
            try:
                self.exitcodes = int(config.get(name_prog, "exitcodes"))
            except configparser.ParsingError:
                self.exitcodes = 0
            try:
                self.startsecs = int(config.get(name_prog, "startsecs"))
            except configparser.ParsingError:
                self.startsecs = 1
            try:
                self.startretries = int(config.get(name_prog, "startretries"))
            except configparser.ParsingError:
                self.startretries = 3
            try:
                self.stopsignal = config.get(name_prog, "stopsignal")
            except configparser.ParsingError:
                self.stopsignal = "TERM"
            try:
                self.stopwaitsecs = config.get(name_prog, "stopwaitsecs")
            except configparser.ParsingError:
                self.stopwaitsecs = 10
            try:
                self.stdout = config.get(name_prog, "stdout_logfile")
            except configparser.ParsingError:
                self.stdout = None
            try:
                self.stderr = config.get(name_prog, "stderr_logfile")
            except configparser.ParsingError:
                self.stderr = None
            try: 
                self.env = config.get(name_prog, "environnement")
            except configparser.ParsingError:
                self.env = None
            try:
                self.dir = config.get(name_prog, "directory")
            except configparser.ParsingError:
                self.dir = None
            try:
                self.umask = config.get(name_prog, "umask")
            except configparser.ParsingError:
                self.umask = None 
            self.status = "STARTING"

    def conf(self):
        DG(" conf") 

        try:
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
