# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __main__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/04 21:57:30 by ariard            #+#    #+#              #
#    Updated: 2017/04/13 00:27:18 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import os
import sys
import signal
import time
import socket
import configparser

from daemonize import *
from server import *
from monitor import *
from log import *
from debug import *

if __name__ == '__main__' :
    
    DG_init()
    if len(sys.argv) < 2:
        print("usage : <config_file>")
        exit(-1)

    DG("start")
    daemonize()
    log = log()
    config = configparser.ConfigParser()
    config.read_file(open('/Users/ariard/Projects/taskmaster/taskmasterd/master.config'))
    monitor = Monitor(config, (config.sections()))
    monitor.launch_all()
#   server.init
    server = Server('', 2121)
#   server.launch
    server.accept()
    server.receive()
    DG("usual end")


#server.init #server.listen #server.deploy #server.exit
