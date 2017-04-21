# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    taskmasterd.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/04 21:57:30 by ariard            #+#    #+#              #
#    Updated: 2017/04/21 17:52:05 by echo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import os
import sys
import signal
import time
import socket
import configparser
import threading

from daemonize import *
from server import *
from monitor import *
from log import *
from debug import *

log = log()

if __name__ == '__main__' :
    
    DG_init()
    if len(sys.argv) < 2:
        print("usage : <config_file>")
        exit(-1)
    DG("start")
    daemonize()
    log.update("[SERVER] - File Configuration Sourced\n")
    config = configparser.ConfigParser()
    config.read_file(open('/Users/echo/taskmaster/taskmasterd/master.config'))
    monitor = Monitor(config, (config.sections()))
    monitor.start_reporter()
    monitor.start_guardian()
    monitor.launch_all()
#   server.init
    DG(str(table_prog)) 
    server = Server('', 4242)
    DG("after launch server")
#   server.launch
    while True:
        global num_threads
        server.c, server.addr = server.ss.accept()
        DG("after accept")
        print('Connection received from : ', server.addr)
        DG("after received")
        server.c.send(str(num_threads).encode('utf-8'))
        t = threading.Thread(target=new_client, args=(server.c, server.addr))
        t.start()
        num_threads += 1
        print('debug: [' + str(num_threads) + '] threads are actually running')
    server.ss.close()
    DG("usual end")

#server.init #server.listen #server.deploy #server.exit
