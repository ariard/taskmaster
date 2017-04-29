# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 04:23:04 by ariard            #+#    #+#              #
#    Updated: 2017/04/29 17:48:48 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import configparser

from debug import *

class Program:
    def __init__(self, config , name_prog):
            try:
                self.command = config.get(name_prog, "command")
            except configparser.NoOptionError:
                self.command = None
            try:
                self.numprocs = int(config.get(name_prog, "numprocs"))
            except configparser.NoOptionError:
                self.numprocs = 1
            try:
                self.autostart = config.get(name_prog, "autostart")
            except configparser.NoOptionError:
                self.autostart = "true"
            try:
                self.autorestart = config.get(name_prog, "autorestart")
            except configparser.NoOptionError:
                self.autorestart = "unexpected" 
            self.exitcodes = list()
            try:
                self.exitcodes.append(config.get(name_prog, "exitcodes").split(','))
            except configparser.NoOptionError:
                self.exitcodes.append(0)
            try:
                self.startsecs = int(config.get(name_prog, "startsecs"))
            except configparser.NoOptionError:
                self.startsecs = 1
            try:
                self.startretries = int(config.get(name_prog, "startretries"))
            except configparser.NoOptionError:
                self.startretries = 3
            try:
                self.stopsignal = config.get(name_prog, "stopsignal")
            except configparser.NoOptionError:
                self.stopsignal = "TERM"
            try:
                self.stopwaitsecs = config.get(name_prog, "stopwaitsecs")
            except configparser.NoOptionError:
                self.stopwaitsecs = 10
            try:
                self.stdout = config.get(name_prog, "stdout_logfile")
            except configparser.NoOptionError:
                self.stdout = "/dev/null"
            try:
                self.stderr = config.get(name_prog, "stderr_logfile")
            except configparser.NoOptionError:
                self.stderr = "/dev/null"
            try: 
                self.env = config.get(name_prog, "environnement")
            except configparser.NoOptionError:
                self.env = None
            try:
                self.dir = config.get(name_prog, "directory")
            except configparser.NoOptionError:
                self.dir = None
            try:
                self.umask = config.get(name_prog, "umask")
            except configparser.NoOptionError:
                self.umask = None 

    def conf(self):
        if self.dir:
            os.chdir(self.dir) 

        if self.umask:
            os.umask(int(self.umask))
        
        if self.env:
            list_env = self.env.split(',')
            for i in list_env:
                j = i.split('=')
                os.environ[j[0]] = j[1]

        if self.stdout:
            fd = open(self.stdout, 'w+')
            os.dup2(fd.fileno(), 1)

        if self.stderr:
            fd = open(self.stderr, 'w+')
            os.dup2(fd.fileno(), 2)
