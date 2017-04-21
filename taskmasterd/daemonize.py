# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    daemonize.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/06 23:34:11 by ariard            #+#    #+#              #
#    Updated: 2017/04/21 17:36:30 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys
import signal

from debug import *

def daemon_success(number, frame):
    file = open("/tmp/daemon.log", 'w+')
    file.write(str(os.times()) + "\n")
    file.write("Your daemon has been successfully created !")
    file.close()
    sys.exit()

def daemonize():

#   Close all non standard fd
#   Restore default signal handler
#   Sanitize environnement variable
#   Check .pid to ensure non-daemon

    DG("before daemonize")
    fatherpid = os.getpid()
    status = os.fork()

    if status > 0:
       signal.signal(signal.SIGUSR1, daemon_success)
       os.wait()
    
    if status == 0:
        os.setsid()
        status = os.fork()
        
        if status > 0:
            sys.exit()

        fd = open('/dev/null')
        os.dup2(fd.fileno(), 0)
#         os.dup2(fd.fileno(), 1)
#        os.dup2(fd.fileno(), 2)

        os.umask(0)
        os.chdir('/')
        
        pidfile = open('/tmp/taskmasterd.pid', 'w+')
        pid = os.getpid() 
        pidfile.write(str(pid))

        os.kill(fatherpid, signal.SIGUSR2) 
