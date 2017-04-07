# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __main__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/04 21:57:30 by ariard            #+#    #+#              #
#    Updated: 2017/04/07 04:27:42 by ariard           ###   ########.fr        #
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

if __name__ == '__main__' :
    
    if len(sys.argv) < 2:
        print("usage : <config_file>")
        exit(-1)

    daemonize()
    log = log()
    config = configparser.ConfigParser()
    config.read_file(open('/Users/ariard/Projects/taskmaster/taskmasterd/master.config'))
    monitor = monitor(config, (config.sections()))
    monitor.launch()
    server = server('', 2121)
    server.accept()
    server.receive()


#server.init #server.listen #server.deploy #server.exit
